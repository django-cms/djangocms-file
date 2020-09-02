from cms.api import add_plugin, create_page
from cms.test_utils.testcases import CMSTestCase

from djangocms_file.cms_plugins import FilePlugin, FolderPlugin

from .helpers import get_filer_file, get_filer_folder


class FilePluginsTestCase(CMSTestCase):

    def setUp(self):
        self.language = "en"
        self.home = create_page(
            title="home",
            template="page.html",
            language=self.language,
        )
        self.home.publish(self.language)
        self.page = create_page(
            title="content",
            template="page.html",
            language=self.language,
        )
        self.page.publish(self.language)
        self.placeholder = self.page.placeholders.get(slot="content")
        self.superuser = self.get_superuser()
        self.file = get_filer_file()
        self.folder = get_filer_folder()

    def tearDown(self):
        self.page.delete()
        self.home.delete()
        self.superuser.delete()
        if self.file:
            self.file.delete()
            del self.file
            with self.assertRaises(AttributeError):
                print(self.file)
        if self.folder:
            self.folder.delete()
            del self.folder
            with self.assertRaises(AttributeError):
                print(self.folder)

    def test_file_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=FilePlugin.__name__,
            language=self.language,
            file_src=self.file,
        )
        plugin.full_clean()  # should not raise an error
        self.assertEqual(plugin.plugin_type, "FilePlugin")

    def test_folder_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=FolderPlugin.__name__,
            language=self.language,
            folder_src=self.folder,
        )
        plugin.full_clean()  # should not raise an error
        self.assertEqual(plugin.plugin_type, "FolderPlugin")

    def test_plugin_structure(self):
        request_url = self.page.get_absolute_url(self.language) + "?toolbar_off=true"

        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=FilePlugin.__name__,
            language=self.language,
            file_src=self.file,
        )
        self.page.publish(self.language)
        self.assertEqual(plugin.get_plugin_class_instance().name, "File")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertContains(response, "test_file.pdf")

        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=FolderPlugin.__name__,
            language=self.language,
            folder_src=self.folder,
        )
        self.page.publish(self.language)
        self.assertEqual(plugin.get_plugin_class_instance().name, "Folder")

        with self.login_user_context(self.superuser):
            response = self.client.get(request_url)

        self.assertContains(response, "No files were found in the specified folder.")

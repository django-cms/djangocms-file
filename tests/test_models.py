from django.conf import settings
from django.test import TestCase

from djangocms_file.models import LINK_TARGET, File, Folder, get_templates

from .helpers import get_filer_file, get_filer_folder


class CommonModelTestCase(TestCase):

    def test_settings(self):
        self.assertEqual(get_templates(), [('default', 'Default')])
        settings.DJANGOCMS_FILE_TEMPLATES = [('feature', 'Feature')]
        self.assertEqual(get_templates(), [('default', 'Default'), ('feature', 'Feature')])


class FileModelTestCase(TestCase):

    def setUp(self):
        self.file = get_filer_file()

    def tearDown(self):
        if self.file:
            self.file.delete()
            del self.file
            with self.assertRaises(AttributeError):
                print(self.file)
        File.objects.filter(pk=1).delete()
        self.assertEqual(File.objects.all().count(), 0)

    def test_file_instance(self):
        File.objects.create(
            template="default",
            file_src=self.file,
            file_name="some file",
            link_target=LINK_TARGET[0][0],
            link_title="some link title",
            show_file_size=True,
            attributes="{'data-type', 'file'}",
        )
        instance = File.objects.all()
        self.assertEqual(len(instance), 1)
        instance = File.objects.get(pk=1)
        self.assertEqual(instance.template, "default")
        self.assertEqual(instance.file_src, self.file)
        self.assertEqual(instance.file_name, "some file")
        self.assertEqual(instance.link_target, "_self")
        self.assertEqual(instance.show_file_size, True)
        self.assertEqual(instance.attributes, "{'data-type', 'file'}")
        # old copy relation and test methods
        instance.copy_relations(instance)
        self.assertEqual(instance.__str__(), "test_file.pdf")
        self.assertEqual(instance.get_short_description(), "some file")
        instance.file_name = None
        self.assertEqual(instance.get_short_description(), "test_file.pdf")
        instance.file_src = None
        self.assertEqual(instance.__str__(), "1")
        self.assertEqual(instance.get_short_description(), "<file is missing>")


class FolderModelTestCase(TestCase):

    def setUp(self):
        self.folder = get_filer_folder()
        self.file = get_filer_file()

    def tearDown(self):
        if self.file:
            self.file.delete()
            del self.file
            with self.assertRaises(AttributeError):
                print(self.file)
        Folder.objects.filter(pk=1).delete()
        self.assertEqual(File.objects.all().count(), 0)

    def test_folder_instance(self):
        Folder.objects.create(
            template="default",
            folder_src=self.folder,
            link_target=LINK_TARGET[0][0],
            show_file_size=True,
            attributes="{'data-type', 'folder'}",
        )
        instance = Folder.objects.all()
        self.assertEqual(len(instance), 1)
        instance = Folder.objects.get(pk=1)
        self.assertEqual(instance.template, "default")
        self.assertEqual(instance.folder_src, self.folder)
        self.assertEqual(instance.link_target, "_self")
        self.assertEqual(instance.show_file_size, True)
        self.assertEqual(instance.attributes, "{'data-type', 'folder'}")
        # old copy relation and test methods
        instance.copy_relations(instance)
        self.assertEqual(instance.__str__(), "test_folder")
        self.assertEqual(instance.get_short_description(), "test_folder")
        instance.folder_src = None
        self.assertEqual(instance.__str__(), "1")
        self.assertEqual(instance.get_short_description(), "<folder is missing>")
        # get files
        self.assertEqual(instance.get_files(), [])
        self.file = get_filer_file(
            folder=self.folder
        )
        instance = Folder.objects.create(
            folder_src=self.folder,
        )
        self.assertEqual(instance.get_files(), [self.file])

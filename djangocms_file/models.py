import os

from django.db import models
from django.conf import settings
from django.core.files.storage import default_storage
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
try:
    from cms.models import get_plugin_media_path
except ImportError:
    def get_plugin_media_path(instance, filename):
        """
        See cms.models.pluginmodel.get_plugin_media_path on django CMS 3.0.4+
        for information
        """
        return instance.get_media_path(filename)
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class File(CMSPlugin):
    """
    Plugin for storing any type of file.

    Default template displays download link with icon (if available) and file
    size.

    Icons are searched for within <MEDIA_ROOT>/<CMS_FILE_ICON_PATH>
    (CMS_FILE_ICON_PATH is a plugin-specific setting which defaults to
    "<CMS_MEDIA_PATH>/img/icons/filetypes") with filenames of the form
    <file_ext>.<icon_ext>, where <file_ext> is the extension of the file
    itself, and <icon_ext> is one of <CMS_FILE_ICON_EXTENSIONS> (another plugin
     specific setting, which defaults to ('gif', 'png'))

    This could be updated to use the mimetypes library to determine the type of
    file rather than storing a separate icon for each different extension.

    The icon search is currently performed within get_icon_url; this is
    probably a performance concern.
    """
    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin, related_name='djangocms_file_file', parent_link=True)

    file = models.FileField(_("file"), upload_to=get_plugin_media_path)
    title = models.CharField(
        _("title"), max_length=255, null=True, blank=True,
        help_text=_("Optional title to display. If not supplied, the filename "
                    "will be used."))
    target = models.CharField(
        _("target"), blank=True, max_length=100, choices=((
            ("", _("same window")),
            ("_blank", _("new window")),
            ("_parent", _("parent window")),
            ("_top", _("topmost frame")),
        )), default='', help_text=_("Optional link target."))
    tooltip = models.CharField(
        _("tooltip"), blank=True, max_length=255,
        help_text=_("Optional tooltip."))
    # CMS_ICON_EXTENSIONS and CMS_ICON_PATH are assumed to be plugin-specific,
    # and not included in cms.settings -- they are therefore imported
    # from django.conf.settings
    ICON_EXTENSIONS = getattr(
        settings, "CMS_FILE_ICON_EXTENSIONS", ('gif', 'png'))
    ICON_PATH = getattr(
        settings, "CMS_FILE_ICON_PATH",
        os.path.join(settings.STATIC_ROOT, "cms", "img", "icons/filetypes"))

    ICON_URL = getattr(
        settings, "CMS_FILE_ICON_URL", "%s%s/%s/%s/" % (
            settings.STATIC_URL, "cms", "img", "icons/filetypes"))

    def __str__(self):
        if self.title:
            return self.title
        elif self.file:
            # added if, because it raised attribute error when
            # file wasn't defined
            return self.get_file_name()
        return "<empty>"

    def get_icon_url(self):
        path_base = os.path.join(self.ICON_PATH, self.get_ext())
        url_base = '%s%s' % (self.ICON_URL, self.get_ext())
        for ext in self.ICON_EXTENSIONS:
            if os.path.exists("%s.%s" % (path_base, ext)):
                return "%s.%s" % (url_base, ext)
        return None

    def file_exists(self):
        return default_storage.exists(self.file.name)

    def get_file_name(self):
        return os.path.basename(self.file.name)

    def get_ext(self):
        return os.path.splitext(self.get_file_name())[1][1:].lower()

    search_fields = ('title',)

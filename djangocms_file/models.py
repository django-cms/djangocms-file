# -*- coding: utf-8 -*-
"""
Enables the user to add a "File" plugin that displays a file wrapped by
an <anchor> tag.
"""
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin

from djangocms_attributes_field.fields import AttributesField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField


LINK_TARGET = (
    ('_self', _('Open in same window')),
    ('_blank', _('Open in new window')),
    ('_parent', _('Delegate to parent')),
    ('_top', _('Delegate to top')),
)


# Add additional choices through the ``settings.py``.
def get_templates():
    choices = [
        ('default', _('Default')),
    ]
    choices += getattr(
        settings,
        'DJANGOCMS_FILE_TEMPLATES',
        [],
    )
    return choices


@python_2_unicode_compatible
class AbstractFile(CMSPlugin):
    """
    Renders a file wrapped by an anchor
    """
    search_fields = ('name',)

    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    file_src = FilerFileField(
        verbose_name=_('File'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    file_name = models.CharField(
        verbose_name=_('Name'),
        blank=True,
        max_length=255,
        help_text=_('Overrides the default file name with the given value.'),
    )
    link_target = models.CharField(
        verbose_name=_('Link target'),
        choices=LINK_TARGET,
        blank=True,
        max_length=255,
        default='',
    )
    link_title = models.CharField(
        verbose_name=_('Link title'),
        blank=True,
        max_length=255,
    )
    show_file_size = models.BooleanField(
        verbose_name=_('Show file size'),
        blank=True,
        default=False,
        help_text=_('Appends the file size at the end of the name.'),
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['href', 'title', 'target'],
    )

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    def __str__(self):
        if self.file_src and self.file_src.label:
            return self.file_src.label
        return str(self.pk)

    def get_short_description(self):
        if self.file_src and self.file_name:
            return self.file_name
        if self.file_src and self.file_src.label:
            return self.file_src.label
        return ugettext('<file is missing>')

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey, it's required to copy over
        # the reference from the instance to the new plugin.
        self.file_src = oldinstance.file_src


@python_2_unicode_compatible
class AbstractFolder(CMSPlugin):
    """
    Renders a folder plugin to the selected tempalte
    """
    template = models.CharField(
        verbose_name=_('Template'),
        choices=get_templates(),
        default=get_templates()[0][0],
        max_length=255,
    )
    folder_src = FilerFolderField(
        verbose_name=_('Folder'),
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    link_target = models.CharField(
        verbose_name=_('Link target'),
        choices=LINK_TARGET,
        blank=True,
        max_length=255,
        default='',
    )
    show_file_size = models.BooleanField(
        verbose_name=_('Show file size'),
        blank=True,
        default=False,
        help_text=_('Appends the file size at the end of the name.'),
    )
    attributes = AttributesField(
        verbose_name=_('Attributes'),
        blank=True,
        excluded_keys=['href', 'target'],
    )

    # Add an app namespace to related_name to avoid field name clashes
    # with any other plugins that have a field with the same name as the
    # lowercase of the class name of this model.
    # https://github.com/divio/django-cms/issues/5030
    cmsplugin_ptr = models.OneToOneField(
        CMSPlugin,
        related_name='%(app_label)s_%(class)s',
        parent_link=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True

    def __str__(self):
        if self.folder_src and self.folder_src.name:
            return self.folder_src.name
        return str(self.pk)

    def get_short_description(self):
        if self.folder_src and self.folder_src.name:
            return self.folder_src.name
        return ugettext('<folder is missing>')

    def copy_relations(self, oldinstance):
        # Because we have a ForeignKey, it's required to copy over
        # the reference from the instance to the new plugin.
        self.folder_src = oldinstance.folder_src

    def get_files(self):
        if not self.folder_src:
            return []
        return list(self.folder_src.files)


class File(AbstractFile):

    class Meta:
        abstract = False


class Folder(AbstractFolder):

    class Meta:
        abstract = False

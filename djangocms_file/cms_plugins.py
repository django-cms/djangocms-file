# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import File, Folder


class FilePlugin(CMSPluginBase):
    model = File
    name = _('File')
    render_template = 'djangocms_file/file.html'
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'file_src',
                'file_name',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                ('link_target', 'link_title'),
                'show_file_size',
                'attributes',
            )
        }),
    ]


class FolderPlugin(CMSPluginBase):
    model = Folder
    name = _('Folder')
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'template',
                'folder_src',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'link_target',
                'show_file_size',
                'attributes',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_file/{}/folder.html'.format(instance.template)


plugin_pool.register_plugin(FilePlugin)
plugin_pool.register_plugin(FolderPlugin)

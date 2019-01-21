# -*- coding: utf-8 -*-
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import File, Folder


class FilePlugin(CMSPluginBase):
    model = File
    name = _('File')
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
                'template',
                ('link_target', 'link_title'),
                'show_file_size',
                'attributes',
            )
        }),
    ]

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_file/{}/file.html'.format(instance.template)


class FolderPlugin(CMSPluginBase):
    model = Folder
    name = _('Folder')
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': (
                'folder_src',
            )
        }),
        (_('Advanced settings'), {
            'classes': ('collapse',),
            'fields': (
                'template',
                'link_target',
                'show_file_size',
                'attributes',
            )
        }),
    ]

    def render(self, context, instance, placeholder):
        context['folder_files'] = instance.get_files()
        return super(FolderPlugin, self).render(context, instance, placeholder)

    def get_render_template(self, context, instance, placeholder):
        return 'djangocms_file/{}/folder.html'.format(instance.template)


plugin_pool.register_plugin(FilePlugin)
plugin_pool.register_plugin(FolderPlugin)

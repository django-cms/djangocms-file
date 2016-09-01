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


class FolderPlugin(CMSPluginBase):
    model = Folder
    name = _('Folder')
    render_template = 'djangocms_file/folder.html'
    text_enabled = True


plugin_pool.register_plugin(FilePlugin)
plugin_pool.register_plugin(FolderPlugin)

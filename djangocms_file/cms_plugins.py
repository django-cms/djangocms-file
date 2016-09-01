# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import File


class FilePlugin(CMSPluginBase):
    model = File
    name = _('File')
    render_template = 'cms/plugins/file.html'
    text_enabled = True

    fieldsets = [
        (None, {
            'fields': ('title', 'file', 'tooltip', 'target', )
        })
    ]

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            'placeholder': placeholder,
        })
        return context


plugin_pool.register_plugin(FilePlugin)

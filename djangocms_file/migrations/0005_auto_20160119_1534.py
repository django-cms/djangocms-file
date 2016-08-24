# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0004_set_related_name_for_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='source',
            field=models.FileField(upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='source'),
        ),
        migrations.AlterField(
            model_name='file',
            name='target',
            field=models.CharField(blank=True, max_length=100, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], help_text='Optional link target.', default='', verbose_name='target'),
        ),
    ]

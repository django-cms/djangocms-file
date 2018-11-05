# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cms.models.pluginmodel
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, serialize=False, parent_link=True, auto_created=True, to='cms.CMSPlugin', primary_key=True)),
                ('file', models.FileField(verbose_name='file', upload_to=cms.models.pluginmodel.get_plugin_media_path)),
                ('title', models.CharField(verbose_name='title', blank=True, null=True, max_length=255)),
                ('target', models.CharField(verbose_name='target', blank=True, default='', max_length=100, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')])),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

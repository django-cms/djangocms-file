# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.pluginmodel


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('file', models.FileField(upload_to=cms.models.pluginmodel.get_plugin_media_path, verbose_name='file')),
                ('title', models.CharField(max_length=255, null=True, verbose_name='title', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

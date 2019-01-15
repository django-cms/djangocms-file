# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import djangocms_attributes_field.fields
import filer.fields.folder

from djangocms_file.models import get_templates


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
        ('filer', '0006_auto_20160623_1627'),
        ('djangocms_file', '0007_adapted_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('template', models.CharField(default=get_templates()[0][0], max_length=255, verbose_name='Template', choices=get_templates())),
                ('link_target', models.CharField(default='', max_length=255, verbose_name='Link target', blank=True, choices=[('_self', 'Open in same window'), ('_blank', 'Open in new window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')])),
                ('show_file_size', models.BooleanField(default=False, help_text='Appends the file size at the end of the name.', verbose_name='Show file size')),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True)),
                ('cmsplugin_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='djangocms_file_folder', primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('folder_src', filer.fields.folder.FilerFolderField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='Folder', to='filer.Folder', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
import djangocms_attributes_field.fields
import filer.fields.file
from django.db import migrations, models

from djangocms_file.models import get_templates


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0006_migrate_to_filer'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='attributes',
            field=djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Attributes', blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='template',
            field=models.CharField(default=get_templates()[0][0], max_length=255, verbose_name='Template', choices=get_templates()),
        ),
        migrations.RenameField(
            model_name='file',
            old_name='title',
            new_name='file_name',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='target',
            new_name='link_target',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='tooltip',
            new_name='link_title',
        ),
        migrations.AlterField(
            model_name='file',
            name='link_target',
            field=models.CharField(default='', max_length=255, verbose_name='Link target', blank=True, choices=[('_self', 'Open in same window'), ('_blank', 'Open in new window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')]),
        ),
        migrations.AlterField(
            model_name='file',
            name='link_title',
            field=models.CharField(max_length=255, verbose_name='Link title', blank=True),
        ),
        migrations.AddField(
            model_name='file',
            name='show_file_size',
            field=models.BooleanField(default=False, help_text='Appends the file size at the end of the name.', verbose_name='Show file size'),
        ),
        migrations.AlterField(
            model_name='file',
            name='file_src',
            field=filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', to='filer.File', null=True),
        ),
    ]

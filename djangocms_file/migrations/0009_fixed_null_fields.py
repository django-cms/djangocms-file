# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def reset_null_values(apps, schema_editor):
    File = apps.get_model('djangocms_file', 'File')
    plugins = File.objects.all()
    plugins.filter(file_name__isnull=True).update(file_name='')


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0008_add_folder'),
    ]

    operations = [
        migrations.RunPython(reset_null_values),
    ]

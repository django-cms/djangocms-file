# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models

import filer.fields.file


def migrate_to_filer(apps, schema_editor):
    # Because filer is polymorphic, Djangos migration can't handle
    from filer.models import File
    FileInstance = apps.get_model('djangocms_file', 'File')
    plugins = FileInstance.objects.all()

    for plugin in plugins:
        if plugin.file:
            filesrc = File.objects.get_or_create(
                file=plugin.file.file,
                defaults={
                    'name': plugin.file.name,
                }
            )[0]
            plugins.filter(pk=plugin.pk).update(file_src=filesrc)


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0006_auto_20160623_1627'),
        ('djangocms_file', '0005_auto_20160119_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='file_src',
            field=filer.fields.file.FilerFileField(related_name='+', on_delete=django.db.models.deletion.SET_NULL, verbose_name='File', blank=True, to='filer.File', null=True),
        ),
        migrations.RunPython(migrate_to_filer),
        migrations.RemoveField(
            model_name='file',
            name='file',
        ),
    ]

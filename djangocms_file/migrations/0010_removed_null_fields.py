# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0009_fixed_null_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_name',
            field=models.CharField(default='', help_text='Overrides the default file name with the given value.', max_length=255, verbose_name='Name', blank=True),
            preserve_default=False,
        ),
    ]

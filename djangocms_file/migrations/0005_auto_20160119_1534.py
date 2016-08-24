# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0004_set_related_name_for_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='target',
            field=models.CharField(blank=True, max_length=100, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], help_text='Optional link target.', default='', verbose_name='target'),
        ),
    ]

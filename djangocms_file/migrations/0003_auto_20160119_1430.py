# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0002_auto_20151202_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='target',
            field=models.CharField(blank=True, verbose_name='target', help_text='Optional link target.', max_length=100, choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], default=''),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='tooltip',
            field=models.CharField(help_text='Optional tooltip.', max_length=255, verbose_name='tooltip', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='target',
            field=models.CharField(default='', choices=[('', 'same window'), ('_blank', 'new window'), ('_parent', 'parent window'), ('_top', 'topmost frame')], max_length=100, blank=True, help_text='Optional link target.', verbose_name='target'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(help_text='Optional title to display. If not supplied, the filename will be used.', max_length=255, null=True, verbose_name='title', blank=True),
            preserve_default=True,
        ),
    ]

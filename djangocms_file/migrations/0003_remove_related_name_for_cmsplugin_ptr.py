# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0002_auto_20151202_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='+', serialize=False, to='cms.CMSPlugin'),
        ),
    ]

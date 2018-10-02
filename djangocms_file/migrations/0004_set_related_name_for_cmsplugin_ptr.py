# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_file', '0003_remove_related_name_for_cmsplugin_ptr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='cmsplugin_ptr',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_file_file', serialize=False, to='cms.CMSPlugin'),
        ),
    ]

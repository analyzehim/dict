# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 14:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20161019_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='count_right',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='word',
            name='count_wrong',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

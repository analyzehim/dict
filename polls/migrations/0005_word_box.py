# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20161024_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='box',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

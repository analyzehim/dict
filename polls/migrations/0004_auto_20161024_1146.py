# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20161023_1421'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='isAdjective',
        ),
        migrations.RemoveField(
            model_name='word',
            name='isAdverb',
        ),
        migrations.RemoveField(
            model_name='word',
            name='isNoun',
        ),
        migrations.RemoveField(
            model_name='word',
            name='isVerb',
        ),
        migrations.AddField(
            model_name='word',
            name='speechClass',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

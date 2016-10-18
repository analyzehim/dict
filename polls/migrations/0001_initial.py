# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.PositiveSmallIntegerField(primary_key=True, serialize=False)),
                ('word_eng', models.CharField(max_length=40)),
                ('word_rus', models.CharField(max_length=40)),
                ('example', models.CharField(max_length=400)),
                ('flag', models.IntegerField()),
            ],
        ),
    ]

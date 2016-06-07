# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 15:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asteroid',
            name='exposure_count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='asteroid',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 7, 15, 24, 7, 705162)),
        ),
        migrations.AlterField(
            model_name='asteroid',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 7, 15, 24, 7, 704952)),
        ),
    ]

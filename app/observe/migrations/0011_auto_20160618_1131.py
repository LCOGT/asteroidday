# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 11:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observe', '0010_auto_20160617_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asteroid',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 18, 11, 31, 15, 868404)),
        ),
        migrations.AlterField(
            model_name='asteroid',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 18, 11, 31, 15, 868684)),
        ),
        migrations.AlterField(
            model_name='asteroid',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 18, 11, 31, 15, 868203)),
        ),
        migrations.AlterField(
            model_name='observation',
            name='last_update',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 18, 11, 31, 15, 869815)),
        ),
    ]

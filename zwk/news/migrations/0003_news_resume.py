# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-23 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20180407_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='resume',
            field=models.TextField(default='By Kyroz'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20160615_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='replies_count',
            field=models.IntegerField(default=0, verbose_name='replies count'),
        ),
    ]

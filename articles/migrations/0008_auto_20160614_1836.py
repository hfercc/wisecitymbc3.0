# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-14 10:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20160614_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='name'),
        ),
    ]

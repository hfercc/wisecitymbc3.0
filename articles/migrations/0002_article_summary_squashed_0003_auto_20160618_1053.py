# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-18 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('articles', '0002_article_summary'), ('articles', '0003_auto_20160618_1053')]

    dependencies = [
        ('articles', '0001_initial_squashed_0008_auto_20160614_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='summary',
            field=models.TextField(blank=True, verbose_name='summary'),
        ),
    ]

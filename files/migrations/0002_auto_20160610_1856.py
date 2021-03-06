# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 10:56
from __future__ import unicode_literals

from django.db import migrations
import enhancements.models.fields
import files.consts


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='file_type',
            field=enhancements.models.fields.EnumField(files.consts.FileType, choices=[(files.consts.FileType(1), 'video'), (files.consts.FileType(2), 'image'), (files.consts.FileType(3), 'file')], default=files.consts.FileType(3)),
        ),
    ]

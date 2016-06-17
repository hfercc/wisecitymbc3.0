# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import enhancements.models.fields
import files.consts


class Migration(migrations.Migration):

    replaces = [('files', '0001_initial'), ('files', '0002_auto_20160610_1856'), ('files', '0003_auto_20160616_1911'), ('files', '0004_file_path'), ('files', '0005_auto_20160616_2223')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=4096, verbose_name='file name')),
                ('storage_url', models.URLField(blank=True, verbose_name='url')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='created time')),
                ('mime_type', models.CharField(blank=True, max_length=255, verbose_name='mime type')),
                ('file_type', enhancements.models.fields.EnumField(files.consts.FileType, choices=[(files.consts.FileType(1), 'video'), (files.consts.FileType(2), 'image'), (files.consts.FileType(3), 'file')], default=files.consts.FileType(3), verbose_name='file type')),
                ('path', models.CharField(default='', max_length=4096, verbose_name='file path')),
            ],
        ),
    ]

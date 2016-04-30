# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 13:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0001_squashed_0002_auto_20160430_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='target_content_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='target_id',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
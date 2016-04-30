# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20160429_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.IntegerField(choices=[(1, 'government'), (3, 'bureau'), (2, 'company')], default=2),
        ),
    ]

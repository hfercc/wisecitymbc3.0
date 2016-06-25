# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 14:41
from __future__ import unicode_literals

import accounts.consts
from django.db import migrations
import enhancements.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160502_0414_squashed_0010_auto_20160614_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bureau_type',
            field=enhancements.models.fields.EnumField(accounts.consts.BureauType, choices=[(accounts.consts.BureauType(1), 'none'), (accounts.consts.BureauType(2), 'real_estate'), (accounts.consts.BureauType(3), 'car'), (accounts.consts.BureauType(4), 'electronic_technology'), (accounts.consts.BureauType(5), 'bank'), (accounts.consts.BureauType(6), 'energy_and_raw_materials'), (accounts.consts.BureauType(7), 'financial_system'), (accounts.consts.BureauType(8), 'media')], default=accounts.consts.BureauType(1), editable=False, verbose_name='bureau type'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 10:55
from __future__ import unicode_literals

import accounts.consts
from django.db import migrations
import enhancements.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20160610_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bureau_type',
            field=enhancements.models.fields.EnumField(accounts.consts.BureauType, choices=[(accounts.consts.BureauType(1), 'none'), (accounts.consts.BureauType(2), 'real_estate'), (accounts.consts.BureauType(3), 'car'), (accounts.consts.BureauType(4), 'electronic_technology'), (accounts.consts.BureauType(5), 'bank'), (accounts.consts.BureauType(6), 'enegry_and_raw_materials'), (accounts.consts.BureauType(7), 'financial_system'), (accounts.consts.BureauType(8), 'media')], default=accounts.consts.BureauType(1), verbose_name='bureau type'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=enhancements.models.fields.EnumField(accounts.consts.UserType, choices=[(accounts.consts.UserType(1), 'government'), (accounts.consts.UserType(2), 'company'), (accounts.consts.UserType(3), 'bureau')], default=accounts.consts.UserType(2), verbose_name='user type'),
        ),
    ]

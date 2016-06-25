# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-15 05:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_reply_attachments'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name': 'reply', 'verbose_name_plural': 'replies'},
        ),
        migrations.AlterModelOptions(
            name='topic',
            options={'verbose_name': 'topic', 'verbose_name_plural': 'topics'},
        ),
        migrations.AddField(
            model_name='topic',
            name='title',
            field=models.CharField(default='', max_length=1000, verbose_name='title'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reply',
            name='attachments',
            field=models.ManyToManyField(to='files.File', verbose_name='attachments'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Topic', verbose_name='topic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='asker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='asker'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created time'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='is closed'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='updated time'),
        ),
    ]

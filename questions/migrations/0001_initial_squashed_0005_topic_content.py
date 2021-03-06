# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-17 08:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('questions', '0001_initial'), ('questions', '0002_reply_attachments'), ('questions', '0003_auto_20160615_1326'), ('questions', '0004_topic_replies_count'), ('questions', '0005_topic_content')]

    dependencies = [
        ('files', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now_add=True)),
                ('is_closed', models.BooleanField(default=False)),
                ('asker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reply',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Topic'),
        ),
        migrations.AddField(
            model_name='reply',
            name='attachments',
            field=models.ManyToManyField(to='files.File'),
        ),
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
        migrations.AddField(
            model_name='topic',
            name='replies_count',
            field=models.IntegerField(default=0, verbose_name='replies count'),
        ),
        migrations.AddField(
            model_name='topic',
            name='content',
            field=models.TextField(default='', verbose_name='content'),
            preserve_default=False,
        ),
    ]

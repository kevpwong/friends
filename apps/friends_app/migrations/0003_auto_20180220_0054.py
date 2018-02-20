# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-20 00:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends_app', '0002_auto_20180219_2200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='friends',
        ),
        migrations.AddField(
            model_name='friendship',
            name='friend_friend',
            field=models.ManyToManyField(related_name='friendfriends', to='friends_app.User'),
        ),
        migrations.AddField(
            model_name='friendship',
            name='user_friend',
            field=models.ManyToManyField(related_name='userfriends', to='friends_app.User'),
        ),
    ]

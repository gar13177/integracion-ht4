# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-21 01:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestrator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='id',
        ),
        migrations.AlterField(
            model_name='appuser',
            name='user_token',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
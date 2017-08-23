# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orchestrator', '0005_auto_20170822_0615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstored',
            name='user_token',
            field=models.ForeignKey(db_column='user_token', on_delete=django.db.models.deletion.CASCADE, to='orchestrator.AppUser'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orchestrator', '0006_auto_20170822_0622'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderstored',
            name='status',
            field=models.CharField(default='invoiced', max_length=100),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 09:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lat',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='lng',
            field=models.FloatField(null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-20 17:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171020_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='date',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]

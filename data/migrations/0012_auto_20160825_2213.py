# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-25 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20160810_2225'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='private_key',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='public_key',
            field=models.TextField(blank=True),
        ),
    ]
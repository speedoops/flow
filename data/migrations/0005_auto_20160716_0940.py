# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20160716_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='delete',
        ),
        migrations.AddField(
            model_name='project',
            name='deleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

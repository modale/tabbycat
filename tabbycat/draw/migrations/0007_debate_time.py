# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('draw', '0006_auto_20160228_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='debate',
            name='time',
            field=models.DateTimeField(blank=True, help_text='The time/date of a debate if it is specifically scheduled', null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournaments', '0008_auto_20160202_1955'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='division',
            options={'ordering': ['tournament', 'seq']},
        ),
        migrations.AlterModelOptions(
            name='round',
            options={'ordering': ['tournament', 'seq']},
        ),
        migrations.AlterModelOptions(
            name='tournament',
            options={'ordering': ['seq']},
        ),
    ]

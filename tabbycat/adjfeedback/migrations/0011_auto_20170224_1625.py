# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 16:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adjfeedback', '0010_auto_20160914_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='confirm_timestamp',
            field=models.DateTimeField(blank=True, null=True, verbose_name='confirm timestamp'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='confirmed'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='confirmer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adjfeedback_adjudicatorfeedback_confirmed', to=settings.AUTH_USER_MODEL, verbose_name='confirmer'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True, verbose_name='IP address'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='submitter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='adjfeedback_adjudicatorfeedback_submitted', to=settings.AUTH_USER_MODEL, verbose_name='submitter'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='submitter_type',
            field=models.CharField(choices=[('T', 'Tab room'), ('P', 'Public')], max_length=1, verbose_name='submitter type'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timestamp'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedback',
            name='version',
            field=models.PositiveIntegerField(verbose_name='version'),
        ),
    ]

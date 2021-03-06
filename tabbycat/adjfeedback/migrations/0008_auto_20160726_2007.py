# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 20:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adjfeedback', '0007_from_adj_from_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adjudicatorfeedbackquestion',
            name='from_adj',
            field=models.BooleanField(help_text='Adjudicators should be asked this question (about other adjudicators)'),
        ),
        migrations.AlterField(
            model_name='adjudicatorfeedbackquestion',
            name='from_team',
            field=models.BooleanField(help_text='Teams should be asked this question'),
        ),
    ]

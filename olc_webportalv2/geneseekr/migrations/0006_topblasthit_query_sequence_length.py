# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-11-21 15:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geneseekr', '0005_auto_20181121_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='topblasthit',
            name='query_sequence_length',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

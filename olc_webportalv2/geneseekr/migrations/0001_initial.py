# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-04 15:25
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AzureGeneSeekrTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exit_code_file', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GeneSeekrDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seqid', models.CharField(default='', max_length=24)),
                ('geneseekr_results', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GeneSeekrRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seqids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True, default=[], size=None)),
                ('missing_seqids', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True, default=[], size=None)),
                ('query_sequence', models.CharField(blank=True, max_length=10000)),
                ('status', models.CharField(default='Unprocessed', max_length=64)),
                ('download_link', models.CharField(blank=True, max_length=256)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('geneseekr_type', models.CharField(default='BLASTN', max_length=48)),
                ('geneseekr_results', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True)),
            ],
        ),
    ]

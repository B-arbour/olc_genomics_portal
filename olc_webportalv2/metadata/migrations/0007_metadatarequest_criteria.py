# Generated by Django 2.1.5 on 2019-04-23 17:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0006_auto_20190423_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='metadatarequest',
            name='criteria',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}, null=True),
        ),
    ]
# Generated by Django 2.1.5 on 2019-07-26 18:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geneseekr', '0029_auto_20190726_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='amrsummary',
            name='other_input_files',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default=[], max_length=64), null=True, size=None),
        ),
        migrations.AlterField(
            model_name='amrsummary',
            name='seqids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=24), blank=True, default=[], null=True, size=None),
        ),
    ]
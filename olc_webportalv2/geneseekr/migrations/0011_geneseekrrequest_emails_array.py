# Generated by Django 2.1.5 on 2019-02-18 19:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geneseekr', '0010_auto_20190122_2012'),
    ]

    operations = [
        migrations.AddField(
            model_name='geneseekrrequest',
            name='emails_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.EmailField(max_length=100), blank=True, default=[], size=None),
        ),
    ]

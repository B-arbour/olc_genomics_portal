# Generated by Django 2.2.13 on 2020-08-25 21:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer_finder', '0003_auto_20200825_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primerfinder',
            name='primer_seq',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100), size=None),
        ),
    ]

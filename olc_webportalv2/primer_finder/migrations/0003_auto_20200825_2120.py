# Generated by Django 2.2.13 on 2020-08-25 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer_finder', '0002_primerfinder_primer_seq'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primerfinder',
            name='primer_seq',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

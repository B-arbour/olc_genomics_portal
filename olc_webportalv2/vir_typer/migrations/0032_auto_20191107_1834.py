# Generated by Django 2.1.11 on 2019-11-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0031_auto_20191107_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtyperrequest',
            name='sample_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
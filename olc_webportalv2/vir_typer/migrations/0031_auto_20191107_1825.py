# Generated by Django 2.1.11 on 2019-11-07 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0030_auto_20191107_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='virtyperproject',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]

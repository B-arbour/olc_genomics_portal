# Generated by Django 2.1.5 on 2019-07-23 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0009_auto_20190710_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sequencedata',
            name='olnid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seqids', to='metadata.OLNID'),
        ),
    ]

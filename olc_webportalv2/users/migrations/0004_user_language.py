# Generated by Django 2.1.5 on 2019-08-01 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190312_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en-ca', 'English'), ('fr', 'French')], default='en-ca', max_length=10),
        ),
    ]

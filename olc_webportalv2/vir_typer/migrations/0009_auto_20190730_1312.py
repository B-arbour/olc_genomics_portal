# Generated by Django 2.1.5 on 2019-07-30 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vir_typer', '0008_remove_virtyperproject_emails_array'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='virtyperblobcontainername',
            name='project_name',
        ),
        migrations.DeleteModel(
            name='VirTyperBlobContainerName',
        ),
    ]

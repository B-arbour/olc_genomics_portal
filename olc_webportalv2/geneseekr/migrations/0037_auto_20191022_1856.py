# Generated by Django 2.1.5 on 2019-10-22 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geneseekr', '0036_auto_20191022_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='treeazurerequest',
            old_name='parsnp_request',
            new_name='tree_request',
        ),
    ]

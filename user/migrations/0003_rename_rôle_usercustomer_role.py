# Generated by Django 5.1.6 on 2025-02-11 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_usercustomer_groups_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usercustomer',
            old_name='rôle',
            new_name='role',
        ),
    ]

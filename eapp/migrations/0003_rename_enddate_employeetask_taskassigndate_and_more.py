# Generated by Django 4.2.1 on 2023-05-21 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eapp', '0002_remove_employeetask_contact_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeetask',
            old_name='enddate',
            new_name='taskassigndate',
        ),
        migrations.RemoveField(
            model_name='employeetask',
            name='joiningdate',
        ),
    ]

# Generated by Django 3.1.2 on 2020-10-19 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20201018_1625'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usermessage',
            old_name='undread',
            new_name='unread',
        ),
    ]

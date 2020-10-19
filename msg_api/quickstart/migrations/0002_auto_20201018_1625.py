# Generated by Django 3.1.2 on 2020-10-18 16:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('quickstart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessage',
            name='creation_date',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='receiver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sent_messages', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='usermessage',
            name='undread',
            field=models.BooleanField(default=True),
        ),
    ]

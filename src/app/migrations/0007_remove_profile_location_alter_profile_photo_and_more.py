# Generated by Django 4.2.11 on 2024-05-22 11:04

import app.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_profile_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Location',
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=app.utils.user_directory_path),
        ),
        migrations.AddField(
            model_name='profile',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.location'),
        ),
    ]

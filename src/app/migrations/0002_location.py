# Generated by Django 4.2.8 on 2024-04-29 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=128)),
                ('address_2', models.CharField(default=True, max_length=123)),
                ('city', models.CharField(max_length=120)),
            ],
        ),
    ]

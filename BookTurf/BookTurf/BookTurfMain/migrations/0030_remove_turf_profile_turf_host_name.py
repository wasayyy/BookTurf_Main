# Generated by Django 4.1.10 on 2023-10-17 14:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BookTurfMain', '0029_turf_host'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turf_profile',
            name='turf_host_name',
        ),
    ]

# Generated by Django 4.1.10 on 2023-09-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookTurfMain', '0014_alter_turf_profile_turf_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='addmin',
            fields=[
                ('addmin_id', models.AutoField(primary_key=True, serialize=False)),
                ('addmin_username', models.CharField(default='', max_length=100)),
                ('addmin_password', models.CharField(default='', max_length=100)),
            ],
        ),
    ]

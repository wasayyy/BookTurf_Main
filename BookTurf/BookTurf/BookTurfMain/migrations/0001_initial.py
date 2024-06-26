# Generated by Django 4.1.10 on 2023-08-07 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turf_Pics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('turf_picture', models.ImageField(upload_to='BookTurf/BookTurfMain/media/BookTurfMain')),
            ],
        ),
        migrations.CreateModel(
            name='Turf_Profile',
            fields=[
                ('turf_id', models.AutoField(primary_key=True, serialize=False)),
                ('turf_name', models.CharField(default='', max_length=100)),
                ('turf_rating', models.IntegerField(default=0, max_length=1)),
                ('turf_category', models.CharField(default='', max_length=100)),
                ('turf_description', models.CharField(default='', max_length=300)),
                ('turf_rules_regulations', models.CharField(default='', max_length=300)),
                ('turf_address', models.CharField(default='Please enter the address owner', max_length=200)),
                ('turf_ownerContact_number', models.IntegerField(default=9999999991, max_length=10)),
                ('turf_reviews', models.CharField(default='', max_length=200)),
                ('turf_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='BookTurfMain.turf_pics')),
            ],
        ),
        migrations.CreateModel(
            name='Turf_Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.CharField(default='', max_length=200)),
                ('rating', models.IntegerField(default=0)),
                ('Review_Turf_Profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='BookTurfMain.turf_profile')),
            ],
        ),
    ]

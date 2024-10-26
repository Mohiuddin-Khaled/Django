# Generated by Django 5.1 on 2024-10-26 09:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_image', models.ImageField(blank=True, null=True, upload_to='car/media/uploads/')),
                ('car_name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('car_price', models.FloatField()),
                ('car_brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car.brandmodel')),
                ('car_buyer', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
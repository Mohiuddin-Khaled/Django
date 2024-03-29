# Generated by Django 5.0.1 on 2024-02-04 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('father_name', models.CharField(max_length=30)),
                ('mother_name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=50)),
                ('date', models.DateTimeField()),
                ('payment_slip', models.FileField(upload_to='files/')),
                ('gadget_name', models.CharField(max_length=60)),
                ('ip_address', models.GenericIPAddressField()),
                ('correct_info', models.BooleanField(null=True)),
            ],
        ),
    ]

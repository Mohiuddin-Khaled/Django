# Generated by Django 5.1 on 2024-09-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelApp', '0002_alter_studentmodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='date',
            field=models.DateField(help_text='Date Format: yyyy-mm-dd'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='ip_address',
            field=models.GenericIPAddressField(help_text='Example: 103.137.160.108'),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='name',
            field=models.CharField(help_text='Write your full name', max_length=20),
        ),
    ]

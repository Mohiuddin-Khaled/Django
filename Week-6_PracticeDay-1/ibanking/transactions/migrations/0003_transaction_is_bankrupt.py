# Generated by Django 5.1 on 2024-11-29 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_alter_transaction_transaction_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='is_bankrupt',
            field=models.BooleanField(default=False),
        ),
    ]

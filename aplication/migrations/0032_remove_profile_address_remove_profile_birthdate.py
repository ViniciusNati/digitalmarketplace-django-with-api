# Generated by Django 4.1.5 on 2023-01-11 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0031_remove_profile_cart_remove_profile_verified_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='birthdate',
        ),
    ]
# Generated by Django 4.1.5 on 2023-01-09 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0023_remove_profile_address_remove_profile_birthdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='profile',
            name='releasebalance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]

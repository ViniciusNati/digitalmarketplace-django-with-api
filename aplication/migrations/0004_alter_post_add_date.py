# Generated by Django 4.1.5 on 2023-01-09 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0003_alter_post_add_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

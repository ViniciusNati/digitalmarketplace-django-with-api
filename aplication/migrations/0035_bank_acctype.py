# Generated by Django 4.1.5 on 2023-01-11 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0034_bank_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='acctype',
            field=models.CharField(default='Membro', max_length=20),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-09 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0024_alter_profile_balance_alter_profile_releasebalance'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='verified',
            name='photorg',
            field=models.ImageField(null=True, upload_to='documents/'),
        ),
    ]
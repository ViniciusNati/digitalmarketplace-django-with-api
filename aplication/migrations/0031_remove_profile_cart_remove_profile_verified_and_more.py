# Generated by Django 4.1.5 on 2023-01-11 11:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplication', '0030_alter_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='verified',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

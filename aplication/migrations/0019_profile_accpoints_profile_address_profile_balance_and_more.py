# Generated by Django 4.1.5 on 2023-01-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplication', '0018_profile_delete_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='accpoints',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='balance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cep',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='country',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='cpf',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='membersince',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='online',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='releasebalance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='rg',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telefone',
            field=models.IntegerField(null=True),
        ),
    ]

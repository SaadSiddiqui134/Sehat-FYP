# Generated by Django 5.1.5 on 2025-01-25 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userManagement', '0002_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UserPassword',
            field=models.CharField(max_length=255),
        ),
    ]

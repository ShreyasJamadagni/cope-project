# Generated by Django 2.1.7 on 2019-03-26 03:35

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('admin', '0004_auto_20190326_0335'),
        ('articles', '0013_auto_20190326_0335'),
        ('auth', '0009_alter_user_last_name_max_length'),
        ('users', '0005_auto_20190326_0309'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Member',
        ),
    ]

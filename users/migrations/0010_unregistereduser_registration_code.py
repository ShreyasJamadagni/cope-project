# Generated by Django 2.1.7 on 2019-03-26 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_unregistereduser'),
    ]

    operations = [
        migrations.AddField(
            model_name='unregistereduser',
            name='registration_code',
            field=models.TextField(default='passed'),
            preserve_default=False,
        ),
    ]

# Generated by Django 2.1.7 on 2019-03-25 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20190325_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
    ]

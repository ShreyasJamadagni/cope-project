# Generated by Django 2.1.7 on 2019-03-25 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_remove_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='user',
        ),
    ]

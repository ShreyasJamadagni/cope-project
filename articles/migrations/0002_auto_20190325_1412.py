# Generated by Django 2.1.7 on 2019-03-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='Shreyas'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(max_length=90),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-25 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210624_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='body',
        ),
        migrations.AddField(
            model_name='profile',
            name='club',
            field=models.CharField(default='', max_length=100),
        ),
    ]

# Generated by Django 4.1.1 on 2022-10-05 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweet', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweetmodel',
            name='profile',
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-15 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodeLibrary', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myreferences',
            name='articlePublishedBy',
        ),
    ]

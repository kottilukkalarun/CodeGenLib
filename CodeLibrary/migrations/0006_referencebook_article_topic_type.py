# Generated by Django 3.0.6 on 2020-05-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeLibrary', '0005_auto_20200516_1605'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencebook',
            name='article_topic_type',
            field=models.CharField(choices=[('Epiplex', 'Epiplex'), ('UiPath', 'UiPath'), ('Python', 'Python'), ('C#.net', 'C#.net'), ('C#.net', 'C#.net'), ('Bootstrap', 'Bootstrap'), ('Javascript', 'Javascript')], default='Epiplex', max_length=100),
        ),
    ]

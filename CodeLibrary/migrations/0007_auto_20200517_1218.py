# Generated by Django 3.0.6 on 2020-05-17 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeLibrary', '0006_referencebook_article_topic_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencebook',
            name='article_topic_type',
            field=models.CharField(choices=[('Epiplex', 'Epiplex'), ('UiPath', 'UiPath'), ('Python', 'Python'), ('C#.net', 'C#.net'), ('HTML', 'HTML'), ('Bootstrap', 'Bootstrap'), ('Javascript', 'Javascript')], default='Epiplex', max_length=100),
        ),
    ]

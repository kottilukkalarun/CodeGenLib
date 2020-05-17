# Generated by Django 3.0.6 on 2020-05-15 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeLibrary', '0003_auto_20200515_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='referencebook',
            name='article_updated_by',
            field=models.CharField(choices=[('admin', 'Arun Kesavan'), ('user', 'Others')], default='user', max_length=500),
        ),
    ]

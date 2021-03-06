# Generated by Django 3.0.6 on 2020-05-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CodeLibrary', '0004_referencebook_article_updated_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='referencebook',
            name='article_updated_by',
            field=models.CharField(choices=[('admin', 'Arun Kesavan'), ('user', 'Others')], default='admin', max_length=500),
        ),
        migrations.AlterField(
            model_name='referencebook',
            name='last_updated_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

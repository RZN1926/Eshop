# Generated by Django 5.0.6 on 2024-07-11 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_titale_news_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='article',
            field=models.TextField(),
        ),
    ]

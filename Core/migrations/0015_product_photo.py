# Generated by Django 5.0.6 on 2024-07-26 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='prods/', verbose_name='photo'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-12 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_profile_rename_user_views_product_costumer_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views_qty',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 5.0.6 on 2024-07-24 15:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0012_product_create_at_product_expiration_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='quarantee',
            new_name='guarantee',
        ),
    ]
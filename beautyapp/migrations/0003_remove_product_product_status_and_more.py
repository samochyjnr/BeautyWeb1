# Generated by Django 4.2.4 on 2023-08-17 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0002_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='specification',
        ),
    ]
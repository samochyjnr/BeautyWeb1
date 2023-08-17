# Generated by Django 4.2.4 on 2023-08-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautyapp', '0006_cartorder_wishlist_productview_productimage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_status',
            field=models.CharField(choices=[('draft', 'Processing'), ('disabled', 'Shipped'), ('rejected', 'Rejected'), ('review', 'In Review'), ('published', 'Published')], default='In Review', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, null=True),
        ),
    ]

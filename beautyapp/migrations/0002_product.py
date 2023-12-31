# Generated by Django 4.2.4 on 2023-08-17 06:19

import beautyapp.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beautyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(default='product.jpg', upload_to=beautyapp.models.user_directory_path)),
                ('description', models.TextField(default='Enter your product Description')),
                ('price', models.DecimalField(decimal_places=2, default='400.00', max_digits=8888888)),
                ('old_price', models.DecimalField(decimal_places=2, default='600.00', max_digits=888888888888)),
                ('specification', models.TextField(blank=True, null=True)),
                ('product_status', models.CharField(choices=[('draft', 'Processing'), ('disabled', 'Shipped'), ('rejected', 'Rejected'), ('review', 'In Review'), ('published', 'Published')], default='In Review', max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('in_stock', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('digital', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautyapp.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products',
            },
        ),
    ]

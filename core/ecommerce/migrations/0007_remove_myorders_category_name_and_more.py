# Generated by Django 5.0 on 2024-01-18 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0006_alter_image_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myorders',
            name='category_name',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='item_name',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='item_sku',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='price',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='product_type',
        ),
        migrations.RemoveField(
            model_name='myorders',
            name='quantity',
        ),
    ]

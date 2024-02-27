# Generated by Django 5.0 on 2024-02-08 11:50

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0029_order_label_url_order_tracking_url_provider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontmedia',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/frontEnd'),
        ),
        migrations.AlterField(
            model_name='frontmedia',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='static/videos/frontEnd'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/images/product_images'),
        ),
        migrations.AlterField(
            model_name='item',
            name='main_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[190, 200], upload_to='static/images/product_main_image'),
        ),
    ]
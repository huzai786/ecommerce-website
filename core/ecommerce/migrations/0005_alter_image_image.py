# Generated by Django 5.0 on 2024-01-18 08:35

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=[190, 190], upload_to='static/images'),
        ),
    ]

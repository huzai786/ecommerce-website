# Generated by Django 5.0 on 2024-01-30 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0019_alter_cart_session_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttype',
            name='product_type_slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
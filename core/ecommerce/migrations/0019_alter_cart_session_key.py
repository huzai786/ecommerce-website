# Generated by Django 5.0 on 2024-01-30 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0018_alter_cart_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session_key',
            field=models.CharField(max_length=40),
        ),
    ]

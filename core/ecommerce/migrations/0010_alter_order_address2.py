# Generated by Django 5.0 on 2024-01-18 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0009_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address2',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]

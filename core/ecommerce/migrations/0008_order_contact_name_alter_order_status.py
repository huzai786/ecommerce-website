# Generated by Django 5.0 on 2024-01-18 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_remove_myorders_category_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contact_name',
            field=models.CharField(default='huzzi', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('PENDING', 'PENDING'), ('DELIVERED', 'DELIVERED')], default='PENDING', max_length=50),
        ),
    ]
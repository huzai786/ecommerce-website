# Generated by Django 5.0 on 2024-02-01 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0028_userdetails_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='label_url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='tracking_url_provider',
            field=models.CharField(max_length=500, null=True),
        ),
    ]

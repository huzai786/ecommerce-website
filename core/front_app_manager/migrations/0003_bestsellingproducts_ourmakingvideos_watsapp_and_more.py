# Generated by Django 4.2 on 2024-02-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front_app_manager', '0002_partners'),
    ]

    operations = [
        migrations.CreateModel(
            name='BestSellingProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_sku', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Best Selling item list',
                'verbose_name_plural': 'Best Selling item list',
            },
        ),
        migrations.CreateModel(
            name='OurMakingVideos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(blank=True, null=True, upload_to='static/videos/making_videos')),
            ],
            options={
                'verbose_name': 'Our Making Vidos',
                'verbose_name_plural': 'Our Making Vidos',
            },
        ),
        migrations.CreateModel(
            name='Watsapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Watsapp Number',
                'verbose_name_plural': 'Watsapp Number',
            },
        ),
        migrations.AlterModelOptions(
            name='partners',
            options={'verbose_name': 'Partners', 'verbose_name_plural': 'Partners'},
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-11 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-16 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(upload_to='static/'),
        ),
    ]
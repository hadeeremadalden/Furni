# Generated by Django 4.2.4 on 2023-08-16 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_alter_product_productimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='productImage',
            field=models.ImageField(blank=True, max_length=10000000000000, null=True, upload_to=''),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-17 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_pouplarproduct'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='Image',
            field=models.ImageField(blank=True, max_length=10000000000000, null=True, upload_to=''),
        ),
    ]

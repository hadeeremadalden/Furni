# Generated by Django 4.2.4 on 2023-08-17 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0003_rename_serivceimage_services_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='Image1',
            field=models.ImageField(blank=True, max_length=10000000000000, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='Image2',
            field=models.ImageField(blank=True, max_length=10000000000000, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='testimonials',
            name='Image3',
            field=models.ImageField(blank=True, max_length=10000000000000, null=True, upload_to=''),
        ),
    ]
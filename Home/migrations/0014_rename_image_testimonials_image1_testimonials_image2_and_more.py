# Generated by Django 4.2.4 on 2023-08-17 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_testimonials_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonials',
            old_name='Image',
            new_name='Image1',
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

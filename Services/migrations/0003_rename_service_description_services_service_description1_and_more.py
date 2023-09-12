# Generated by Django 4.2.4 on 2023-08-17 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0002_rename_serivceimage_services_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='service_description',
            new_name='service_description1',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='service_title',
            new_name='service_title1',
        ),
        migrations.AddField(
            model_name='services',
            name='service_description2',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='service_description3',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='service_description4',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='service_title2',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='service_title3',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='services',
            name='service_title4',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]

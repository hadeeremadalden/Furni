# Generated by Django 4.2.4 on 2023-08-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('headerImage', models.ImageField(blank=True, max_length=10000000000000, null=True, upload_to='')),
            ],
        ),
    ]

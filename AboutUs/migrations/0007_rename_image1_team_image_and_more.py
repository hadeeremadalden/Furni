# Generated by Django 4.2.4 on 2023-08-18 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AboutUs', '0006_delete_abouus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='Image1',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='description1',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='name1',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='role1',
            new_name='role',
        ),
        migrations.RemoveField(
            model_name='team',
            name='Image2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='Image3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='Image4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='description2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='description3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='description4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='name4',
        ),
        migrations.RemoveField(
            model_name='team',
            name='role2',
        ),
        migrations.RemoveField(
            model_name='team',
            name='role3',
        ),
        migrations.RemoveField(
            model_name='team',
            name='role4',
        ),
    ]
# Generated by Django 3.2.9 on 2021-12-01 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0003_remove_image_field'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Photo',
        ),
    ]
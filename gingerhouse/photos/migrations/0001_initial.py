# Generated by Django 3.2.9 on 2021-12-01 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('houses', '0003_remove_image_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, help_text='Ginger house image. Horizontal format, cropped to 812x680 px.', max_length=255, null=True, upload_to='uploads/', verbose_name='Ginger house image')),
                ('is_primary', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True)),
                ('house', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='houses.gingerhouse')),
            ],
        ),
    ]
# Generated by Django 2.2.10 on 2020-12-05 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='gingerhouse',
            old_name='address',
            new_name='display_address',
        ),
        migrations.AddField(
            model_name='gingerhouse',
            name='image',
            field=models.ImageField(blank=True, help_text='Ginger house image. Horizontal format, cropped to 812x680 px.', max_length=255, null=True, upload_to='uploads/', verbose_name='Ginger house image'),
        ),
        migrations.AddField(
            model_name='gingerhouse',
            name='model_address',
            field=models.TextField(blank=True),
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('ginger_house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='houses.GingerHouse')),
            ],
        ),
        migrations.AddField(
            model_name='gingerhouse',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='houses.Category'),
            preserve_default=False,
        ),
    ]
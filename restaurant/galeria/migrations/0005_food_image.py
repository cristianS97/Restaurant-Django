# Generated by Django 3.1.5 on 2021-01-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0004_food_in_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='image',
            field=models.ImageField(default=None, upload_to='static/img', verbose_name='Imagen'),
        ),
    ]
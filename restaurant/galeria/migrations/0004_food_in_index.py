# Generated by Django 3.1.5 on 2021-01-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_food_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='in_index',
            field=models.BooleanField(default=False, verbose_name='Muestra en inicio'),
        ),
    ]

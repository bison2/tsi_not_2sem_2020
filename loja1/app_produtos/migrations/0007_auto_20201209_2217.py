# Generated by Django 3.1.4 on 2020-12-10 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_produtos', '0006_auto_20201209_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]

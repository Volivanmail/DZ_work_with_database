# Generated by Django 3.1.2 on 2021-11-27 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20211127_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(),
        ),
    ]
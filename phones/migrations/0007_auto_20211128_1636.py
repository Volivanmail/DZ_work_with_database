# Generated by Django 3.1.2 on 2021-11-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0006_auto_20211128_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.URLField(),
        ),
    ]

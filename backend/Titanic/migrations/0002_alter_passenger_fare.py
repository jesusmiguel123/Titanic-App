# Generated by Django 4.2.4 on 2023-08-18 03:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Titanic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='Fare',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0.0, 'Fare must be >= 0'), django.core.validators.MaxValueValidator(600.0, 'Fare must be <= 600')]),
        ),
    ]
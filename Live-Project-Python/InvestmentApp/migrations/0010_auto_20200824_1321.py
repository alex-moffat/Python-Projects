# Generated by Django 2.2.5 on 2020-08-24 20:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvestmentApp', '0009_auto_20200824_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='open_cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, validators=[django.core.validators.MinValueValidator(0.01)], verbose_name='Open/Share'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='quantity',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Quantity'),
        ),
    ]

# Generated by Django 2.2.5 on 2020-08-24 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvestmentApp', '0010_auto_20200824_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='close_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Close/Share'),
        ),
    ]

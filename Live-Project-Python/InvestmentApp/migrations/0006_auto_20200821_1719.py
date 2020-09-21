# Generated by Django 2.2.5 on 2020-08-22 00:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvestmentApp', '0005_auto_20200821_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='close',
            field=models.DateField(blank=True, null=True, verbose_name='Close Date'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='close_cost',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True, verbose_name='Close/Share'),
        ),
        migrations.AlterField(
            model_name='trade',
            name='open',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Open Date'),
        ),
    ]

# Generated by Django 2.2.5 on 2020-08-21 23:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InvestmentApp', '0003_auto_20200820_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='open',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True, verbose_name='Open Date'),
        ),
    ]
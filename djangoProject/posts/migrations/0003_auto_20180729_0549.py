# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-07-29 05:49
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=datetime.datetime(2018, 7, 29, 5, 49, 53, 799608)),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.IntegerField(),
        ),
    ]

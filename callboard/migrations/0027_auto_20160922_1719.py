# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-22 14:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0026_goods_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='rate',
            field=models.IntegerField(default=0, verbose_name='Рейтинг'),
        ),
    ]

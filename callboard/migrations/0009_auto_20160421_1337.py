# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 10:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0008_goods_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.IntegerField(verbose_name='Цена'),
        ),
    ]
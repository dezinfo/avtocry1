# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-04 09:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0033_remove_goods_is_aukc'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='is_aukc1',
            field=models.BooleanField(default=False, verbose_name='На аукционе'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 12:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0058_auto_20161212_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategory_set', to='callboard.SubCategory', verbose_name='Подкатегория'),
        ),
    ]

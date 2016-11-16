# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0052_attribute_filtering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='type',
            field=models.CharField(choices=[('choice', 'Справочник'), ('text', 'Текст'), ('number', 'Число')], default='text', max_length=15, verbose_name='Тип поля'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='rate',
            field=models.PositiveIntegerField(default=0, max_length=1, verbose_name='Рейтинг'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='salles_price',
            field=models.PositiveIntegerField(blank=True, default=0, verbose_name='Цена распродажи'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='views',
            field=models.PositiveIntegerField(default=0, verbose_name='Просмотров'),
        ),
    ]

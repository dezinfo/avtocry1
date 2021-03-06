# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-06 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('callboard', '0013_goods_subtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auctions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_price', models.IntegerField(verbose_name='Начальная цена')),
                ('price_range', models.IntegerField(verbose_name='Мин шаг цены')),
                ('extra_price', models.IntegerField(verbose_name='Экспрес продажа')),
                ('start_date', models.DateTimeField(verbose_name='Дата начала аукциона')),
                ('end_date', models.DateTimeField(verbose_name='Дата завершения аукциона')),
                ('is_active', models.BooleanField(verbose_name='Активно')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date update')),
                ('lot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callboard.Goods', verbose_name='Лот')),
            ],
        ),
    ]

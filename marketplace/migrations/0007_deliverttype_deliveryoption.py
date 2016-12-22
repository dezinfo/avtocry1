# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 14:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_auto_20161205_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelivertType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Транспортная компания')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option_name', models.CharField(max_length=60, verbose_name='Опция доставки')),
                ('delivery_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.DelivertType')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advdesk', '0002_advertisement_creation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
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
        migrations.AlterField(
            model_name='subcategory',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]

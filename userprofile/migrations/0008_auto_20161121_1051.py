# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0007_auto_20161114_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofiletable',
            name='user_image',
            field=models.ImageField(blank=True, default='/static//images/avatar.jpeg', upload_to='', verbose_name='Аватар'),
        ),
    ]

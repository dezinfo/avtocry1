# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-10 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0045_auto_20161103_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='verbos_name',
            field=models.CharField(max_length=50),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 13:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_auto_20160320_1732'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='good',
        ),
        migrations.RemoveField(
            model_name='orderitems',
            name='order',
        ),
        migrations.DeleteModel(
            name='OrderItems',
        ),
    ]
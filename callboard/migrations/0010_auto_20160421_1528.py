# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 12:28
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0009_auto_20160421_1337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='description',
            field=tinymce.models.HTMLField(verbose_name='Описание'),
        ),
    ]
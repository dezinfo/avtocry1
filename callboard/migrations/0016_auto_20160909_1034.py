# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-09 07:34
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0015_remove_subtype_subcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='subtype',
        ),
        migrations.AddField(
            model_name='goods',
            name='type',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='subcategory', chained_model_field='subcategory', default=1, on_delete=django.db.models.deletion.CASCADE, to='callboard.Type', verbose_name='Тип'),
            preserve_default=False,
        ),
    ]

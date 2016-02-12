# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 10:42
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('advdesk', '0005_auto_20160210_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='subcategory_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='advdesk.SubCategory', verbose_name='Подкатегория'),
        ),
    ]

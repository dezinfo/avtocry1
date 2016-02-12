# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 10:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('advdesk', '0004_auto_20160210_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='category_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='advdesk.Category', verbose_name='Карегория'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='goods',
            name='subcategory_id',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category_id', chained_model_field='category_id', on_delete=django.db.models.deletion.CASCADE, to='advdesk.SubCategory', verbose_name='Подкатегория'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-12 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('callboard', '0056_goods_attributes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='city',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='state', chained_model_field='state', null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.Cities', verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='state',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='states', to='userprofile.States', verbose_name='Область'),
        ),
    ]

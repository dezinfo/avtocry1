# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-10 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advdesk', '0007_auto_20160210_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='attribute',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]

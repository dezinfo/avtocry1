# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-05 15:25
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_auto_20161205_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiletable',
            name='dilivery_adress',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]

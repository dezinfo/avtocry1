# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-13 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0008_auto_20161004_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bets',
            name='auction',
        ),
        migrations.AddField(
            model_name='auction',
            name='winner_bet',
            field=models.ManyToManyField(blank=True, null=True, related_name='winner_bets', to='auction.Bets'),
        ),
    ]

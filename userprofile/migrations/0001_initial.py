# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-22 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Inbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('Unread', 'Не прочитано'), ('Readed', 'Прочитано')], max_length=20)),
                ('subject', models.CharField(blank=True, max_length=300)),
                ('body', models.TextField(blank=True)),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL)),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='States',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(blank=True, default='/static/images/avatar.jpeg', upload_to='', verbose_name='Аватар')),
                ('discount_percent', models.IntegerField(default=5, verbose_name='Процент скидки')),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='Телефон')),
                ('skype', models.CharField(blank=True, max_length=100, null=True, verbose_name='Скайп')),
                ('adress_city', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='state', chained_model_field='state', on_delete=django.db.models.deletion.CASCADE, to='userprofile.Cities', verbose_name='Город')),
                ('adress_state', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userprofile.States', verbose_name='Область')),
                ('favorites', models.ManyToManyField(blank=True, related_name='favorited_by_user', to=settings.AUTH_USER_MODEL)),
                ('username', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cities',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.States'),
        ),
    ]

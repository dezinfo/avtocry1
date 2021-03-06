# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-07 11:02
from __future__ import unicode_literals

import callboard.models
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
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя аттрибута')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True, verbose_name='Категория')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('slug', models.SlugField(blank=True, max_length=60)),
                ('follow', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('price', models.IntegerField(blank=True, verbose_name='Цена')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date_update')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callboard.Category', verbose_name='Карегория')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GoodsImageGallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=callboard.models.get_upload_file_name)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callboard.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Подкатегория')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('slug', models.SlugField(blank=True, max_length=60)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callboard.Category', verbose_name='Карегория')),
                ('follow', models.ManyToManyField(blank=True, related_name='sub_category', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='SubCategoryAttr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attrname', models.ForeignKey(max_length=30, on_delete=django.db.models.deletion.CASCADE, to='callboard.Attributes', verbose_name='Аттрибут')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='callboard.Category', verbose_name='Карегория')),
                ('subcategory', smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='callboard.SubCategory', verbose_name='Подкатегория')),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='subcategory',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, blank=True, chained_field='category', chained_model_field='category', on_delete=django.db.models.deletion.CASCADE, to='callboard.SubCategory', verbose_name='Подкатегория'),
        ),
        migrations.AddField(
            model_name='goods',
            name='user',
            field=models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterUniqueTogether(
            name='subcategoryattr',
            unique_together=set([('category', 'subcategory', 'attrname')]),
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together=set([('category', 'name')]),
        ),
    ]

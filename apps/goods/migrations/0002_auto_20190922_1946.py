# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-09-22 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goodsimage',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_front_image',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images', verbose_name='封面图'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(default='', max_length=300, verbose_name='商品名'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/'),
        ),
    ]

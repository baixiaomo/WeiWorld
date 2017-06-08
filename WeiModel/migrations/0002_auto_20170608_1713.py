# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiaddresscollection',
            name='creator',
            field=models.CharField(max_length=20, default='', verbose_name='创建者'),
        ),
        migrations.AddField(
            model_name='weiaddresscollection',
            name='state',
            field=models.CharField(max_length=2, default='', verbose_name='状态'),
        ),
        migrations.AddField(
            model_name='weiaddresscollection',
            name='tags',
            field=models.CharField(max_length=50, default='', verbose_name='地址标签'),
        ),
        migrations.AddField(
            model_name='weiaddresscollection',
            name='type',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='weiaddresscollection',
            name='updater',
            field=models.CharField(max_length=20, default='', verbose_name='修改者'),
        ),
        migrations.AddField(
            model_name='weiaddresscollection',
            name='url',
            field=models.URLField(default='', verbose_name='地址链接'),
        ),
        migrations.AlterField(
            model_name='weiaddresscollection',
            name='desc',
            field=models.CharField(max_length=100, default='', verbose_name='地址描述'),
        ),
        migrations.AlterField(
            model_name='weiaddresscollection',
            name='name',
            field=models.CharField(max_length=20, default='', verbose_name='地址名称'),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0012_auto_20170615_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiindexmodel',
            name='createTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 10, 37, 59, 754167, tzinfo=utc), verbose_name='创建时间', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='creator',
            field=models.CharField(max_length=20, verbose_name='创建者', blank=True),
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='updateTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 15, 10, 38, 9, 472722, tzinfo=utc), verbose_name='更新时间', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='updater',
            field=models.CharField(max_length=20, verbose_name='修改者', blank=True),
        ),
    ]

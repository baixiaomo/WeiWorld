# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0002_auto_20170608_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiaddresscollection',
            name='createTime',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 6, 8, 9, 33, 31, 240168, tzinfo=utc), verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='weiaddresscollection',
            name='updateTime',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 8, 9, 33, 34, 715515, tzinfo=utc), verbose_name='更新时间', auto_now_add=True),
            preserve_default=False,
        ),
    ]

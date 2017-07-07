# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0014_auto_20170615_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weiindexmodel',
            name='createTime',
            field=models.DateTimeField(null=True, auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='updateTime',
            field=models.DateTimeField(blank=True, verbose_name='更新时间', null=True),
        ),
    ]

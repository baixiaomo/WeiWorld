# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0013_auto_20170615_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weiindexmodel',
            name='createTime',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='updateTime',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='更新时间'),
        ),
    ]

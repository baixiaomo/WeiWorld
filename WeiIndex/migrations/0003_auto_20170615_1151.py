# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0002_auto_20170615_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiindexmodel',
            name='display_world',
            field=models.CharField(default='总有一些文字想要留下', max_length=100),
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='primary_title2_left',
            field=models.CharField(default='常用链接', max_length=20),
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='primary_title2_right',
            field=models.CharField(default='百小陌', max_length=20),
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='sub_title2',
            field=models.CharField(default='总有一些文字想要留下', max_length=50),
        ),
    ]

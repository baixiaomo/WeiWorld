# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0005_weidictionary'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeiEssay',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='文章名称', default='', max_length=20)),
                ('content', models.TextField(verbose_name='文章内容')),
                ('author', models.CharField(verbose_name='文章作者', max_length=20)),
                ('type', models.IntegerField(default=0)),
                ('tags', models.CharField(verbose_name='文章标签', default='', max_length=50)),
                ('state', models.CharField(verbose_name='状态', default='', max_length=2)),
                ('creator', models.CharField(verbose_name='创建者', default='', max_length=20)),
                ('updater', models.CharField(verbose_name='修改者', default='', max_length=20)),
                ('createTime', models.DateTimeField(verbose_name='创建时间', auto_now=True)),
                ('updateTime', models.DateTimeField(verbose_name='更新时间', auto_now_add=True)),
            ],
        ),
    ]

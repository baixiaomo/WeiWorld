# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0007_weiaddresscollection_show_in_index'),
        ('WeiIndex', '0016_auto_20170616_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeiIndexModel',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=20, default='模板')),
                ('primary_title', models.CharField(max_length=20, default='我的微世界')),
                ('sub_title', models.CharField(max_length=50, default='副标题')),
                ('enter_button_text', models.CharField(max_length=20, default='进入世界')),
                ('state', models.BooleanField(default=False)),
                ('loginUrl', models.URLField(default='')),
                ('primary_title2_left', models.CharField(max_length=20, default='常用链接')),
                ('primary_title2_right', models.CharField(max_length=20, default='百小陌')),
                ('sub_title2', models.CharField(max_length=50, default='总有一些文字想要留下')),
                ('about_button_text', models.CharField(max_length=20, default='关于我')),
                ('creator', models.CharField(max_length=20, blank=True, verbose_name='创建者')),
                ('updater', models.CharField(max_length=20, blank=True, verbose_name='修改者')),
                ('createTime', models.DateTimeField(auto_now_add=True, verbose_name='创建时间', null=True)),
                ('updateTime', models.DateTimeField(blank=True, verbose_name='更新时间', null=True)),
                ('display_essay', models.ForeignKey(to='WeiModel.WeiEssay', default=1)),
            ],
            options={
                'verbose_name_plural': '[进入微世界]页面',
                'verbose_name': '[进入微世界]页面',
            },
        ),
    ]

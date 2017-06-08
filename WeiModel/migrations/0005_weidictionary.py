# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0004_weifilescollection'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeiDictionary',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('type', models.CharField(verbose_name='字典大类', max_length=100)),
                ('type_desc', models.CharField(verbose_name='字典大类描述', max_length=100)),
                ('code', models.CharField(verbose_name='字典CODE', max_length=100)),
                ('code_desc', models.CharField(verbose_name='CODE描述', max_length=100)),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='字典创建时间')),
                ('modify_time', models.DateTimeField(auto_now_add=True, verbose_name='字典修改时间')),
                ('creator', models.CharField(verbose_name='创建者', max_length=100)),
                ('modifier', models.CharField(blank=True, verbose_name='修改者', max_length=100)),
            ],
        ),
    ]

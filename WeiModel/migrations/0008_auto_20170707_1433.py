# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0007_weiaddresscollection_show_in_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weidictionary',
            options={'verbose_name': '数据字典管理', 'verbose_name_plural': '数据字典管理'},
        ),
        migrations.AddField(
            model_name='weidictionary',
            name='state',
            field=models.BooleanField(verbose_name='状态', default=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0006_weiessay'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiaddresscollection',
            name='show_in_index',
            field=models.BooleanField(verbose_name='是否显示在index页面', default=False),
        ),
    ]

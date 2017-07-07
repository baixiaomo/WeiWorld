# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0004_auto_20170615_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weiindexmodel',
            name='display_world',
            field=models.CharField(default='展示一些文字<br>比如一首诗', max_length=100),
        ),
    ]

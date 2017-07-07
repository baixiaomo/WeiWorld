# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0003_auto_20170615_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weiindexmodel',
            name='display_world',
            field=models.CharField(max_length=100, default='展示一些文字<br>一些想留下来的'),
        ),
    ]

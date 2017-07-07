# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0009_auto_20170615_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weiindexmodel',
            name='display_world',
        ),
    ]

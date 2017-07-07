# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0015_auto_20170615_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weiindexmodel',
            name='display_essay',
        ),
        migrations.DeleteModel(
            name='WeiIndexModel',
        ),
    ]

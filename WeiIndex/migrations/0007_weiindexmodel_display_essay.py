# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0006_weiessay'),
        ('WeiIndex', '0006_auto_20170615_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiindexmodel',
            name='display_essay',
            field=models.ForeignKey(to='WeiModel.WeiEssay', default=1),
        ),
    ]

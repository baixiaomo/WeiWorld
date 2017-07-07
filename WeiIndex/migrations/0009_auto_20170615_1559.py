# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0008_auto_20170615_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weiindexmodel',
            name='display_essay',
            field=models.ForeignKey(default=1, to='WeiModel.WeiEssay'),
        ),
    ]

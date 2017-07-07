# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0011_weiindexmodel_collections_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weiindexmodel',
            name='collections_address',
        ),
        migrations.RemoveField(
            model_name='weiindexmodel',
            name='page1_background_img_url',
        ),
        migrations.RemoveField(
            model_name='weiindexmodel',
            name='page2_background_img_url',
        ),
    ]

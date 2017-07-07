# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0010_remove_weiindexmodel_display_world'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiindexmodel',
            name='collections_address',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

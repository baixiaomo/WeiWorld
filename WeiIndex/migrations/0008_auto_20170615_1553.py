# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0007_weiindexmodel_display_essay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weiindexmodel',
            name='display_essay',
            field=models.ForeignKey(null=True, blank=True, to='WeiModel.WeiEssay', on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]

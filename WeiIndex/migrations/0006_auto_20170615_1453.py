# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0005_auto_20170615_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiindexmodel',
            name='about_button_text',
            field=models.CharField(max_length=20, default='关于我'),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='display_world',
            field=models.CharField(blank=True, max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='page1_background_img_url',
            field=models.CharField(blank=True, max_length=30, default=''),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='page2_background_img_url',
            field=models.CharField(blank=True, max_length=30, default=''),
        ),
    ]

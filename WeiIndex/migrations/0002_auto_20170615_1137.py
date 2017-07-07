# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiIndex', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weiindexmodel',
            name='loginUrl',
            field=models.URLField(default=''),
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='page1_background_img_url',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='weiindexmodel',
            name='page2_background_img_url',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='enter_button_text',
            field=models.CharField(default='进入世界', max_length=20),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='name',
            field=models.CharField(default='模板', max_length=20),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='state',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='weiindexmodel',
            name='sub_title',
            field=models.CharField(default='副标题', max_length=50),
        ),
    ]

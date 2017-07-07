# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeiIndexModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('primary_title', models.CharField(default='我的微世界', max_length=20)),
                ('sub_title', models.CharField(max_length=50)),
                ('enter_button_text', models.CharField(max_length=20)),
                ('state', models.BooleanField()),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeiModel', '0003_auto_20170608_1733'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeiFilesCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('fileName', models.CharField(max_length=100)),
                ('fileType', models.CharField(max_length=2)),
                ('filePath', models.FileField(upload_to='uploads/%Y/%m/%d/')),
                ('uploadTime', models.DateTimeField(auto_now=True)),
                ('uploader', models.CharField(max_length=20)),
                ('fileState', models.CharField(max_length=2)),
                ('fileSort', models.IntegerField()),
            ],
        ),
    ]

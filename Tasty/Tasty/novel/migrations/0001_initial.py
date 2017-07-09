# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('workdate', models.DateTimeField(auto_now=True, verbose_name='\u6536\u5f55\u65f6\u95f4', auto_created=True)),
                ('novelname', models.CharField(max_length=60, verbose_name='\u5c0f\u8bf4\u540d\u79f0')),
                ('author', models.CharField(max_length=100, verbose_name='\u5c0f\u8bf4\u4f5c\u8005')),
                ('url', models.URLField(verbose_name='\u6536\u5f55\u5730\u5740')),
                ('ext1', models.TextField()),
                ('ext2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Novel_detail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('novel_id', models.CharField(max_length=10, verbose_name='\u5c0f\u8bf4id')),
                ('chapter_name', models.CharField(max_length=200, verbose_name='\u7ae0\u8282\u540d\u79f0')),
                ('chapter_text', models.TextField(verbose_name='\u7ae0\u8282\u5185\u5bb9')),
            ],
        ),
    ]

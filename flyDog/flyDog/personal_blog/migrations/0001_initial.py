# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4', auto_created=True)),
                ('release_time', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='\u53d1\u5e03\u65f6\u95f4', db_index=True)),
                ('title', models.CharField(default=b'', max_length=2048, verbose_name='\u5e16\u5b50\u6807\u9898')),
                ('body', models.TextField(verbose_name='\u5e16\u5b50\u5185\u5bb9')),
                ('p_type', models.IntegerField(verbose_name='\u5e16\u5b50\u7c7b\u578b')),
            ],
        ),
        migrations.CreateModel(
            name='Page_struct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=2048, verbose_name='\u5e16\u5b50\u6807\u9898')),
                ('p_type', models.IntegerField(verbose_name='\u5e16\u5b50\u7c7b\u578b')),
                ('rel_type', models.IntegerField(verbose_name='\u5173\u8054\u5e16\u5b50\u7c7b\u578b')),
                ('p_seq', models.IntegerField(verbose_name='\u663e\u793a\u987a\u5e8f')),
            ],
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid', models.IntegerField()),
                ('total', models.IntegerField(default=b'1')),
            ],
        ),
    ]

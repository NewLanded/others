# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('companyName', models.CharField(max_length=100, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('jobBasicInformation', models.TextField(null=True, verbose_name='\u804c\u4f4d\u57fa\u672c\u4fe1\u606f')),
                ('jobAttract', models.TextField(null=True, verbose_name='\u804c\u4f4d\u4f18\u52bf')),
                ('jobDescription', models.TextField(null=True, verbose_name='\u804c\u4f4d\u63cf\u8ff0')),
            ],
        ),
    ]

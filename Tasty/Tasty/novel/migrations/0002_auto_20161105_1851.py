# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='novel',
            name='worktime',
            field=models.CharField(max_length=6, null=True, verbose_name='\u6536\u5f55\u65f6\u95f4'),
        ),
        migrations.AlterField(
            model_name='novel',
            name='workdate',
            field=models.CharField(max_length=8, verbose_name='\u6536\u5f55\u65f6\u95f4'),
        ),
    ]

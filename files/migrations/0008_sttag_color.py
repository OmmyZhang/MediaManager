# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-23 12:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20171107_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='sttag',
            name='color',
            field=models.CharField(default='black', max_length=20),
            preserve_default=False,
        ),
    ]

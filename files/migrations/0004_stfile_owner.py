# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-10-25 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0003_auto_20171021_0511'),
    ]

    operations = [
        migrations.AddField(
            model_name='stfile',
            name='owner',
            field=models.IntegerField(default=-1),
        ),
    ]

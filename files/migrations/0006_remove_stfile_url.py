# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-07 09:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_auto_20171103_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stfile',
            name='url',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-11-03 12:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_stfile_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='stfile',
            name='createDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stfile',
            name='isDir',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stfile',
            name='modifyDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stfile',
            name='size',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stfile',
            name='url',
            field=models.CharField(default='/pic/', max_length=200),
            preserve_default=False,
        ),
    ]

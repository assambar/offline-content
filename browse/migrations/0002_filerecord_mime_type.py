# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browse', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filerecord',
            name='mime_type',
            field=models.CharField(default='text/text', max_length=1024),
            preserve_default=False,
        ),
    ]

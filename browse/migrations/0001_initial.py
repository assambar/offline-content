# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 07:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDirectory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dir_path', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='FileRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_path', models.TextField()),
                ('date_modified', models.DateTimeField(verbose_name='date modified')),
                ('basedir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='browse.BaseDirectory')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-02-02 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_auto_20170131_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_member',
            name='telepon',
            field=models.CharField(blank=True, default='', max_length=18, null=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-20 15:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20170120_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_admin',
            name='avatar',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/avatar,', verbose_name='avatar'),
        ),
    ]

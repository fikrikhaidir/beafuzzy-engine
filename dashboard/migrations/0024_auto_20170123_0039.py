# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-22 17:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_auto_20170122_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='jawaban',
            field=models.TextField(default='', max_length=1500),
        ),
    ]
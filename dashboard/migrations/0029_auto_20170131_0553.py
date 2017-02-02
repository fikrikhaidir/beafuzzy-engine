# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2017-01-30 22:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0028_auto_20170131_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_member',
            name='bukti_organisasi',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/bukti_organisasi', verbose_name='Bukti Organisasi'),
        ),
        migrations.AlterField(
            model_name='data_member',
            name='bukti_prestasi',
            field=models.ImageField(blank=True, default='', null=True, upload_to='upload/bukti_prestasi', verbose_name='Bukti Prestasi'),
        ),
    ]

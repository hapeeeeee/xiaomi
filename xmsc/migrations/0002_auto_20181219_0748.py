# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xmsc', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='phone',
            options={'verbose_name': '手机', 'verbose_name_plural': '手机'},
        ),
        migrations.AddField(
            model_name='phone',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-20 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='phone',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
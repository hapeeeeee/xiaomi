# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-21 03:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('xmsc', '0003_phone_small_img'),
        ('users', '0002_users_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='GouWuche',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='xmsc.Phone', verbose_name='购买商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='购买用户')),
            ],
        ),
    ]

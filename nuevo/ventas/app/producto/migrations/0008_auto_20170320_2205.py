# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-20 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_auto_20170320_2143'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='a_id',
        ),
        migrations.AddField(
            model_name='stock',
            name='almacen',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]

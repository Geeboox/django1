# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 22:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0010_auto_20170324_1805'),
    ]

    operations = [
        migrations.CreateModel(
            name='precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppack', models.DecimalField(decimal_places=2, max_digits=5)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mayorista', models.DecimalField(decimal_places=2, max_digits=5)),
                ('minorista', models.DecimalField(decimal_places=2, max_digits=5)),
                ('agencia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lista', models.DecimalField(decimal_places=2, max_digits=5)),
                ('id_pro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.producto')),
            ],
        ),
    ]

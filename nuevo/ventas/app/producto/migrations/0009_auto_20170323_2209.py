# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-23 22:09
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0008_auto_20170320_2205'),
    ]

    operations = [
        migrations.CreateModel(
            name='precio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ppack', models.DecimalField(decimal_places=2, default=Decimal('0.0000'), max_digits=5)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('mayorista', models.DecimalField(decimal_places=2, max_digits=5)),
                ('minorista', models.DecimalField(decimal_places=2, max_digits=5)),
                ('agencia', models.DecimalField(decimal_places=2, max_digits=5)),
                ('lista', models.DecimalField(decimal_places=2, max_digits=5)),
                ('producto', models.ManyToManyField(blank=True, to='producto.producto')),
            ],
        ),
        migrations.DeleteModel(
            name='precios',
        ),
        migrations.AddField(
            model_name='stock',
            name='producto',
            field=models.ManyToManyField(blank=True, to='producto.producto'),
        ),
    ]

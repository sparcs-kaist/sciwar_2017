# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-16 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20180703_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='type',
            field=models.IntegerField(choices=[(0, 'Sports'), (1, 'Science'), (2, 'Others')], default=0),
        ),
    ]
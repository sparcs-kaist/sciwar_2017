# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-30 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_auto_20180829_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supporter',
            name='size',
            field=models.IntegerField(choices=[(0, 'XS'), (1, 'S'), (2, 'M'), (3, 'L'), (4, 'XL'), (5, 'XXL'), (6, 'XXXL')], default=0),
        ),
    ]
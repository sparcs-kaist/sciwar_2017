# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-18 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20180808_0859'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cheermessage',
            options={'ordering': ['-likes', '-time']},
        ),
        migrations.AddField(
            model_name='location',
            name='left',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='location',
            name='top',
            field=models.IntegerField(default=0),
        ),
    ]

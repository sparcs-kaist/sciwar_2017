# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-18 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180716_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheermessage',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Event'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-08-30 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_auto_20180830_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='players_k',
            field=models.ManyToManyField(blank=True, null=True, related_name='events_k', to='core.Player'),
        ),
        migrations.AlterField(
            model_name='event',
            name='players_p',
            field=models.ManyToManyField(blank=True, null=True, related_name='events_p', to='core.Player'),
        ),
        migrations.AlterField(
            model_name='player',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='position',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]

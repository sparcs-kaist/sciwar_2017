# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 06:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20170721_0208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='name_en',
            new_name='name_eng',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='name_kr',
            new_name='name_kor',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='players_KAIST',
            new_name='players_k',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='players_POSTECH',
            new_name='players_p',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='score_KAIST',
            new_name='score_k',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='score_POSTECH',
            new_name='score_p',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_baseball_KAIST',
            new_name='score_baseball_k',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_baseball_POSTECH',
            new_name='score_baseball_p',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_basketball_KAIST',
            new_name='score_basketball_k',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_basketball_POSTECH',
            new_name='score_basketball_p',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_esports_KAIST',
            new_name='score_esports_k',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_esports_POSTECH',
            new_name='score_esports_p',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_soccer_KAIST',
            new_name='score_soccer_k',
        ),
        migrations.RenameField(
            model_name='totocontent',
            old_name='score_soccer_POSTECH',
            new_name='score_soccer_p',
        ),
        migrations.RemoveField(
            model_name='video',
            name='event',
        ),
        migrations.AddField(
            model_name='video',
            name='event',
            field=models.ManyToManyField(to='core.Event'),
        ),
    ]

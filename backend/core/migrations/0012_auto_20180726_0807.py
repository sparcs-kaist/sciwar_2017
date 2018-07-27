# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-07-26 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20180718_1411'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.IntegerField(choices=[(0, 'NONE'), (1, 'KAIST'), (2, 'POSTECH')])),
                ('name_eng', models.CharField(max_length=30)),
                ('name_kor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Toto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_k', models.IntegerField(blank=True, null=True)),
                ('score_p', models.IntegerField(blank=True, null=True)),
                ('winner', models.IntegerField(choices=[(0, 'NONE'), (1, 'KAIST'), (2, 'POSTECH')])),
                ('bet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toto', to='core.TotoContent')),
            ],
        ),
        migrations.AlterModelOptions(
            name='cheermessage',
            options={'ordering': ['likes']},
        ),
        migrations.AddField(
            model_name='cheermessage',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='core.Location'),
        ),
        migrations.AddField(
            model_name='toto',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toto', to='core.Event'),
        ),
    ]

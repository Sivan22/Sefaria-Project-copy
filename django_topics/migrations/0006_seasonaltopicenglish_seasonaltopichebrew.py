# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-11-27 04:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('django_topics', '0005_auto_20241127_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='SeasonalTopicEnglish',
            fields=[
            ],
            options={
                'verbose_name': 'English Seasonal Topic',
                'verbose_name_plural': 'English Seasonal Topics',
                'proxy': True,
                'indexes': [],
            },
            bases=('django_topics.seasonaltopic',),
        ),
        migrations.CreateModel(
            name='SeasonalTopicHebrew',
            fields=[
            ],
            options={
                'verbose_name': 'Hebrew Seasonal Topic',
                'verbose_name_plural': 'Hebrew Seasonal Topics',
                'proxy': True,
                'indexes': [],
            },
            bases=('django_topics.seasonaltopic',),
        ),
    ]
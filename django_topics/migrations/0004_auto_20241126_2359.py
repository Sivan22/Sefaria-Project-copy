# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2024-11-27 03:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_topics', '0003_auto_20241121_0757'),
    ]

    operations = [
        migrations.AddField(
            model_name='seasonaltopic',
            name='display_date_prefix',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='seasonaltopic',
            name='display_date_suffix',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='seasonaltopic',
            name='lang',
            field=models.CharField(default='en', max_length=255),
            preserve_default=False,
        ),
    ]
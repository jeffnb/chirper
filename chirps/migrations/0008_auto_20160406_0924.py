# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-06 16:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0007_chirp_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='chirp',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='chirp',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chirps', to=settings.AUTH_USER_MODEL),
        ),
    ]
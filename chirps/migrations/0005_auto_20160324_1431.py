# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 21:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0004_auto_20160324_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chirp',
            name='subject',
            field=models.CharField(help_text='Short version as a title of longer chirp message', max_length=50),
        ),
    ]
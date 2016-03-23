# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-23 18:06
from __future__ import unicode_literals

import csv

from django.db import migrations


def load_chirps(apps, schema_editor):
    """
    This is our function to read in a csv file and create Chirps based
    on the data in the file.
    Args:
        apps:
        schema_editor:

    Returns: None

    """
    Chirp = apps.get_model("chirps", "Chirp")

    with open("fixtures/jeff_chirps.csv") as file:
        reader = csv.reader(file)
        lines = [line for line in reader]

    for line in lines:
        chirp = Chirp(message=line[0], subject=line[1], user_id=1)
        chirp.save()


class Migration(migrations.Migration):

    dependencies = [
        ('chirps', '0001_initial'),
    ]

    operations = [
        # Run our function
        migrations.RunPython(load_chirps)
    ]
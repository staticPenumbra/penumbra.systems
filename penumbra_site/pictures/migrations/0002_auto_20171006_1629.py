# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 23:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Media',
            new_name='Picture',
        ),
    ]

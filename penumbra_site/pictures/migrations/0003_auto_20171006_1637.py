# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0002_auto_20171006_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='link',
            field=models.CharField(max_length=200),
        ),
    ]

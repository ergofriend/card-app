# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-22 04:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iniita', '0005_auto_20180122_1009'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
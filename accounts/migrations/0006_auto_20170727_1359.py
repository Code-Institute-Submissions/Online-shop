# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 12:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170727_1348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='udob',
            new_name='dob',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='ugender',
            new_name='gender',
        ),
    ]

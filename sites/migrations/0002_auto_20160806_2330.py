# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Details',
            new_name='Detail',
        ),
        migrations.RenameModel(
            old_name='Sites',
            new_name='Site',
        ),
    ]
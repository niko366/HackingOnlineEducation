# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 09:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0004_auto_20170708_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user_name',
        ),
    ]

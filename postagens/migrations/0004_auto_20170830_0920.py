# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 12:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('postagens', '0003_auto_20170829_0932'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('name',)},
        ),
    ]
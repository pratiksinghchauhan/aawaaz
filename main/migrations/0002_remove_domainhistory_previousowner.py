# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-04 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='domainhistory',
            name='previousOwner',
        ),
    ]
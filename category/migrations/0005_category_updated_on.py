# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 03:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_auto_20161228_0330'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
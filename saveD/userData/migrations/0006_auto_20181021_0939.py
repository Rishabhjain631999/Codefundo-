# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-10-21 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userData', '0005_auto_20181021_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaster',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

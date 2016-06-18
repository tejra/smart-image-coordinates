# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-18 03:27
from __future__ import unicode_literals

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20160618_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='category_name', unique=True),
        ),
        migrations.AlterField(
            model_name='templateformat',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='template_name', unique=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 03:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_identificador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='identificador',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
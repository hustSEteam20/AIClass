# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2019-01-15 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='stu_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='stu_sex',
            field=models.CharField(choices=[('male', '男'), ('female', '女')], default='男', max_length=32),
        ),
    ]

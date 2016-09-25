# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-23 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-published',)},
        ),
        migrations.AddField(
            model_name='article',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('draft', 'DRAFT'), ('published', 'PUBLISHED')], default='draft', max_length=10),
        ),
    ]

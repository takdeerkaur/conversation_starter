# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('topics', '0002_auto_20151124_0511'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]

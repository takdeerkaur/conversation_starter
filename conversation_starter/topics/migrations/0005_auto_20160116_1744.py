# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20160110_1707'),
        ('topics', '0004_auto_20160110_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='category',
        ),
        migrations.AddField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(default=1, to='categories.Category'),
            preserve_default=False,
        ),
    ]

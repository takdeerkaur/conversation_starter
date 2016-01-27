# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0006_auto_20160123_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.ForeignKey(to='categories.Category'),
        ),
    ]

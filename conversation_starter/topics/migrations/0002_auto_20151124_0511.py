# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='category',
            field=models.CharField(default=b'ENT', max_length=3, choices=[(b'ENT', b'Entertainment'), (b'SPO', b'Sports'), (b'ART', b'Art')]),
        ),
    ]

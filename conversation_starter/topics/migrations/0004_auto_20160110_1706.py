# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_auto_20160110_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='topic',
            new_name='topic_name',
        ),
    ]

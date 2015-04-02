# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortnames', '0002_auto_20150331_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='obj',
            name='parents',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]

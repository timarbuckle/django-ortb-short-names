# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shortnames', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='short',
            field=models.CharField(unique=True, max_length=3),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='obj',
            name='short',
            field=models.CharField(unique=True, max_length=30),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('attribute', 'short')]),
        ),
        migrations.AlterUniqueTogether(
            name='obj',
            unique_together=set([('name', 'short')]),
        ),
        migrations.AlterUniqueTogether(
            name='objatt',
            unique_together=set([('obj', 'att')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0012_recipes_ingredient_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipes',
            name='cuisine_ori',
            field=models.CharField(default='', max_length=500),
        ),
    ]

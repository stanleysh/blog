# Generated by Django 2.1.5 on 2019-08-01 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190801_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 1, 14, 20, 43, 520260)),
        ),
    ]

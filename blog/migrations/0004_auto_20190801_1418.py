# Generated by Django 2.1.5 on 2019-08-01 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190801_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='picture',
            new_name='article',
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 8, 1, 14, 17, 56, 923202)),
        ),
    ]

# Generated by Django 2.2.5 on 2019-10-03 08:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(days=7)),
        ),
    ]

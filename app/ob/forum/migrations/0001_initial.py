# Generated by Django 2.2.6 on 2019-10-06 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150)),
                ('user', models.URLField(db_index=True, max_length=150)),
                ('body', models.TextField(db_index=True)),
                ('date_pud', models.DateTimeField(auto_now_add=True)),
                ('views', models.IntegerField(default=0)),
                ('massenge', models.IntegerField(default=0)),
            ],
        ),
    ]

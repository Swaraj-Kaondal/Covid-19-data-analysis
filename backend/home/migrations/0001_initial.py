# Generated by Django 2.2.11 on 2020-06-06 08:25

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Confirmed', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('Active', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('Recovered', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('Deceased', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='tweets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tweet', models.CharField(max_length=200)),
                ('Sentiment', models.CharField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 2.2.11 on 2020-06-08 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200608_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='TweetId',
            field=models.BigIntegerField(),
        ),
    ]

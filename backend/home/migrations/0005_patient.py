# Generated by Django 2.2.11 on 2020-07-13 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200608_1515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.CharField(max_length=100)),
                ('Age', models.IntegerField()),
                ('Id', models.IntegerField()),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=10)),
                ('Status', models.CharField(max_length=100)),
                ('State', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.State')),
            ],
        ),
    ]

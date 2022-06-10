# Generated by Django 4.0.1 on 2022-01-30 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiretuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('tuber_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('tuber_id', models.IntegerField()),
                ('phone', models.CharField(max_length=255)),
                ('user_id', models.IntegerField(blank=True)),
                ('state', models.CharField(max_length=255)),
                ('message', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
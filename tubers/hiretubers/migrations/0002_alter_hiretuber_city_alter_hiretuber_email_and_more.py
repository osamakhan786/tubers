# Generated by Django 4.0.1 on 2022-01-31 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hiretubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hiretuber',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='state',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hiretuber',
            name='tuber_name',
            field=models.CharField(max_length=100),
        ),
    ]

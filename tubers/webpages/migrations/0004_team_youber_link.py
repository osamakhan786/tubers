# Generated by Django 4.0.1 on 2022-01-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youber_link',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]

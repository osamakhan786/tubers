# Generated by Django 4.0.1 on 2022-01-29 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_team_youber_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abouter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='media/slider/%Y/')),
            ],
        ),
    ]

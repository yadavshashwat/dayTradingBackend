# Generated by Django 3.2.11 on 2022-01-22 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historicalTesting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trackedinstruments',
            name='for_data',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='trackedinstruments',
            name='for_strategy',
            field=models.BooleanField(default=False),
        ),
    ]

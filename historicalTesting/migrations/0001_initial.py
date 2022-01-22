# Generated by Django 3.2.11 on 2022-01-22 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InstrumentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('instrument_token', models.CharField(db_index=True, max_length=50)),
                ('exchange_token', models.CharField(db_index=True, max_length=50)),
                ('tradingsymbol', models.CharField(db_index=True, max_length=50)),
                ('name', models.CharField(db_index=True, max_length=100, null=True)),
                ('last_price', models.FloatField()),
                ('expiry', models.DateField(null=True)),
                ('strike', models.FloatField(null=True)),
                ('tick_size', models.FloatField()),
                ('lot_size', models.IntegerField()),
                ('instrument_type', models.CharField(db_index=True, max_length=50)),
                ('segment', models.CharField(db_index=True, max_length=50)),
                ('exchange', models.CharField(db_index=True, max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='tokens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('request_token', models.CharField(max_length=100)),
                ('access_token', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='trackedInstruments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='historicalTesting.instrumentlist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalPricesMinute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('datetime', models.DateTimeField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('volume', models.FloatField()),
                ('tradedate', models.DateField()),
                ('instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='historicalTesting.instrumentlist')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HistoricalPricesDay',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('datetime', models.DateTimeField()),
                ('open_price', models.FloatField()),
                ('high_price', models.FloatField()),
                ('low_price', models.FloatField()),
                ('close_price', models.FloatField()),
                ('volume', models.FloatField()),
                ('tradedate', models.DateField()),
                ('instrument', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='historicalTesting.instrumentlist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

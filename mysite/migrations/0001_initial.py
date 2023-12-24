# Generated by Django 5.0 on 2023-12-24 15:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_id', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Strategy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strategy_id', models.CharField(max_length=10)),
                ('name', models.CharField(help_text='最多10字元', max_length=10)),
                ('profit', models.PositiveIntegerField()),
                ('profit_factor', models.FloatField()),
                ('mdd', models.IntegerField()),
                ('continue_loss', models.PositiveIntegerField()),
                ('hazard_ratio', models.FloatField()),
                ('nums_trade', models.PositiveIntegerField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.commodity')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mysite.session')),
            ],
            options={
                'ordering': ('-pub_date',),
            },
        ),
    ]
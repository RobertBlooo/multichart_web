# Generated by Django 5.0 on 2023-12-24 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_strategy_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='point_value',
            field=models.PositiveIntegerField(default=200),
        ),
    ]

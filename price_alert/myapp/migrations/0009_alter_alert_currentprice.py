# Generated by Django 5.0.7 on 2024-07-30 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alert_currentprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='currentPrice',
            field=models.FloatField(default={'price': 0}),
        ),
    ]

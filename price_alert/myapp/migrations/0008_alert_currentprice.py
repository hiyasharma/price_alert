# Generated by Django 5.0.7 on 2024-07-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_alert_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='currentPrice',
            field=models.FloatField(default=0),
        ),
    ]

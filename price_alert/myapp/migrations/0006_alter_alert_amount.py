# Generated by Django 5.0.7 on 2024-07-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_alert_firstname_alter_alert_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='amount',
            field=models.FloatField(),
        ),
    ]

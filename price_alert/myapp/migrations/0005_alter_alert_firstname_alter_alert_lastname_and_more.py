# Generated by Django 5.0.7 on 2024-07-28 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alert_created_alert_firstname_alert_lastname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='firstName',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='alert',
            name='lastName',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='alert',
            name='status',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='alert',
            name='userEmail',
            field=models.EmailField(max_length=254),
        ),
    ]

# Generated by Django 3.2.22 on 2023-11-08 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20231108_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]

# Generated by Django 3.2.22 on 2023-11-08 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='time',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
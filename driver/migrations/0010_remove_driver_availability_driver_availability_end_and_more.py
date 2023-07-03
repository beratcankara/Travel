# Generated by Django 4.1.7 on 2023-06-05 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0009_driver_availability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='availability',
        ),
        migrations.AddField(
            model_name='driver',
            name='availability_end',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='availability_start',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0008_alter_driver_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='availability',
            field=models.TextField(blank=True, null=True),
        ),
    ]
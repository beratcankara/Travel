# Generated by Django 4.1.7 on 2023-06-05 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0007_remove_driver_confirmpassword'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='driver',
            options={'verbose_name': 'Sürücü', 'verbose_name_plural': 'Sürücü'},
        ),
    ]
# Generated by Django 4.2.2 on 2023-06-09 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_reservation_fiyat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='fiyat',
        ),
    ]
# Generated by Django 4.1.7 on 2023-06-06 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0019_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='arac_resimleri',
        ),
    ]

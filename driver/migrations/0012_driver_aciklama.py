# Generated by Django 4.1.7 on 2023-06-05 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0011_alter_driver_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='aciklama',
            field=models.TextField(null=True),
        ),
    ]

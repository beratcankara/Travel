# Generated by Django 4.1.7 on 2023-06-04 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0003_driver_adres_driver_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='username',
            field=models.CharField(default=' ', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='driver',
            name='profil_fotografi',
            field=models.ImageField(upload_to='images/'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-04 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nUser', '0005_alter_nuser_tc_kimlik'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]

# Generated by Django 4.1.7 on 2023-06-06 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0018_alter_driver_tc_kimlik'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='images/')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='driver.driver')),
            ],
        ),
    ]

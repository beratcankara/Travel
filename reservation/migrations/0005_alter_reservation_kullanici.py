# Generated by Django 4.1.7 on 2023-06-07 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reservation', '0004_reservation_onay_durum_alter_reservation_surucu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='kullanici',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservation_kullanici', to=settings.AUTH_USER_MODEL),
        ),
    ]

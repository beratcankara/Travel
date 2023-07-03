from django.db import models
from django.forms import ValidationError
from driver.models import Driver
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Reservation(models.Model):
    sehir = models.CharField(max_length=100)
    kisi_sayisi = models.PositiveIntegerField()
    baslangic_tarihi = models.DateField()
    bitis_tarihi = models.DateField()
    onay_durum = models.BooleanField(default=False)
    tamam_durum = models.BooleanField(default=False)
    surucu = models.ForeignKey(Driver, on_delete=models.CASCADE, null=True, blank=True, related_name="reservation_surucu")
    kullanici = models.ForeignKey("nUser.nUser", on_delete=models.CASCADE,related_name='reservation_kullanici')
    fiyat = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.sehir} - {self.kullanici.username}"

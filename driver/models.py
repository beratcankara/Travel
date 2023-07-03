from django.db import models


# Create your models here.

class Driver(models.Model):
    ad = models.CharField(max_length=100)
    soyad = models.CharField(max_length=100)
    aciklama = models.TextField(null=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    adres = models.TextField()
    email = models.EmailField()
    tc_kimlik = models.CharField(max_length=11)
    telefon = models.CharField(max_length=20,default="0")
    profil_fotografi = models.ImageField(upload_to='images/')
    arac_marka_model = models.CharField(max_length=100)
    calistigi_sehirler = models.CharField(max_length=200)
    gunluk_tur_fiyati = models.DecimalField(max_digits=8, decimal_places=2)
    availability_start = models.DateTimeField(null=True, blank=True)  # Başlangıç tarihi
    availability_end = models.DateTimeField(null=True, blank=True)  # Bitiş tarihi
    last_login = models.DateTimeField(verbose_name='last login', blank=True, null=True)
    reservation = models.OneToOneField("reservation.Reservation", null=True, blank=True, on_delete=models.SET_NULL, related_name="driver_reservation")
    
    def __str__(self):
        return f"{self.ad} {self.soyad}"
    class Meta:
        verbose_name = "Sürücü"
        verbose_name_plural = "Sürücü"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
class Image(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.driver.ad
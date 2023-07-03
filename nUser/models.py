from django.db import models
from django.contrib.auth.models import AbstractUser
from reservation.models import Reservation

# Create your models here.
class nUser(AbstractUser):
    tc_kimlik = models.CharField(max_length=11)
    adres = models.TextField()
    telefon = models.CharField(max_length=20, default="0")
    email = models.EmailField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    reservation = models.OneToOneField(Reservation, null=True, blank=True, on_delete=models.SET_NULL)
    isDriver = models.BooleanField(default=False)
    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

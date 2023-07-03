from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='city_images')
    description = models.TextField()

    def __str__(self):
        return self.name

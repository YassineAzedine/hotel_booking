from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    image = models.ImageField(upload_to='hotels_images/')
    description = models.TextField()

    def __str__(self):
        return self.name
class Meta:
        verbose_name_plural = "1 - Hotels"
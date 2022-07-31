from tabnanny import verbose
from django.db import models

# Create your models here.


class Data(models.Model):
    country = models.CharField(max_length=100, null=True)
    population = models.PositiveIntegerField(null=True)
    lattitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    # Rename Models in the admin page
    class Meta:
        verbose_name_plural = 'Data'

    def __str__(self):
        return self.country
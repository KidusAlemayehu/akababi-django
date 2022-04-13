from django.db import models

# Create your models here.
class Location(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=5, default=None)
    lng = models.DecimalField(max_digits=8, decimal_places=5, default=None)
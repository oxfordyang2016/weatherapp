from django.db import models

# Create your models here.
class Reading(models.Model):
    location=models.CharField(max_length=1000)
    weather = models.CharField(max_length=1000)
    wind = models.CharField(max_length=1000)
    city = models.CharField(max_length=80,default='yangming is here')

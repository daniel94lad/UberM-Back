from django.db import models

# Create your models here.

class PostalCode(models.Model):
    postalCode = models.IntegerField(unique=True, primary_key=True)
    city = models.CharField(max_length=40)
    state = models.CharField(max_length=40)
    country = models.CharField(max_length=40)
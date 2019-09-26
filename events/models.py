from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    streetAddress = models.CharField(max_length=40)
    # Pending to include the relationship with the postal code
    #postalCode = models.ForeignKey(Ubicacion, related_name='codigo_postal')
    waiterNumber = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

#aqui falta un metodo que retorne las horas trabajadas en el evento
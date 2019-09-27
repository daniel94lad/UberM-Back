from django.db import models
from django.contrib.auth.models import User
from postalcode.models import PostalCode

# Create your models here.
class Event(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
    streetAddress = models.CharField(max_length=40)
    postalCode = models.ForeignKey(PostalCode, on_delete=models.CASCADE)
    waiterNumber = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    score = models.IntegerField(null=True, blank=True)

class EventAssistance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    score = models.IntegerField(null=True, blank=True)

#aqui falta un metodo que retorne las horas trabajadas en el evento
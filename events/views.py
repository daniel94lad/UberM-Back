from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ubermeserosback.serializers import EventSerializer, EventAssistanceSerializer
from events.models import Event, EventAssistance

class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventAssistanceViewSet(ModelViewSet):
    queryset = EventAssistance.objects.all()
    serializer_class = EventAssistanceSerializer
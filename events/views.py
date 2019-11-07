from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from ubermeserosback.serializers import EventSerializer, EventAssistanceSerializer
from events.models import Event, EventAssistance

class EventViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventAssistanceViewSet(ModelViewSet):
    # permission_classes = [IsAuthenticated]
    queryset = EventAssistance.objects.all()
    serializer_class = EventAssistanceSerializer
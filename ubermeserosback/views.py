from django.contrib.auth.models import User
from rest_framework import viewsets
from ubermeserosback.serializers import ProfileSerializer, EventSerializer
from users.models import Profile
from events.models import Event

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
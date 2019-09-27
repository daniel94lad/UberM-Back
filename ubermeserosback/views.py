from django.contrib.auth.models import User
from rest_framework import viewsets
from ubermeserosback.serializers import ProfileSerializer, EventSerializer, PostalCodeSerializer, EventAssistanceSerializer
from users.models import Profile
from events.models import Event, EventAssistance
from postalcode.models import PostalCode

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class PostalCodeViewSet(viewsets.ModelViewSet):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer

class EventAssistanceViewSet(viewsets.ModelViewSet):
    queryset = EventAssistance.objects.all()
    serializer_class = EventAssistanceSerializer
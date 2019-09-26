from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ProfileSerializer, EventSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = EventSerializer
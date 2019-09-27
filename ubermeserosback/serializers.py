from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Profile
from events.models import Event

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['phoneNumber', 'avatar', 'active', 'streetAddress', 'created', 'modified']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['user', 'startDate', 'endDate', 'streetAddress', 'waiterNumber', 'created', 'updated']

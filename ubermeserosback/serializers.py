from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Profile
from events.models import Event

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user','phoneNumber', 'avatar', 'active', 'streetAddress']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Event
        fields = ['user', 'startDate', 'endDate', 'streetAddress', 'waiterNumber', 'score']

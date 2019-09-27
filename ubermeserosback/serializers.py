from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Profile
from events.models import Event, EventAssistance
from postalcode.models import PostalCode

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user','phoneNumber', 'avatar', 'active', 'streetAddress']

class PostalCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostalCode
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    postalCode = PostalCodeSerializer()
    class Meta:
        model = Event
        fields = ['user', 'startDate', 'endDate', 'streetAddress', 'postalCode', 'waiterNumber', 'score']

class EventAssistanceSerializer(serializers.HyperlinkedModelSerializer):
    event = EventSerializer()
    user = UserSerializer()
    class Meta:
        model = EventAssistance
        fields = ['event', 'user', 'accepted', 'score']

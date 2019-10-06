from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import Profile
from events.models import Event, EventAssistance
from postalcode.models import PostalCode

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user','phoneNumber', 'avatar', 'active', 'streetAddress', 'postalCode']

    def create(self, validated_data):
        userData = validated_data.get('user')
        userData['password'] = make_password(userData['password'])
        userInstance = User.objects.create(**userData)
        validated_data['user'] = userInstance
        instance = Profile.objects.create(**validated_data)
        return instance

class PostalCodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PostalCode
        fields = ['postalCode', 'city', 'state', 'country']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['username', 'startDate', 'endDate', 'streetAddress', 'postalCode', 'waiterNumber', 'score']

class EventAssistanceSerializer(serializers.HyperlinkedModelSerializer):
    event = EventSerializer()
    user = UserSerializer()
    class Meta:
        model = EventAssistance
        fields = ['event', 'user', 'accepted', 'score']

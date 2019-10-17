from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token
from users.models import Profile
from events.models import Event, EventAssistance
from postalcode.models import PostalCode

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class TokenSerializer(ModelSerializer):
    #user = UserSerializer()
    class Meta:
        model = Token
        fields = ['key']

class ProfileSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user','phoneNumber', 'avatar', 'active', 'streetAddress', 'postalCode']

    def create(self, validated_data):
        userData = validated_data.get('user')
        userData['password'] = make_password(userData['password'])
        userInstance = User.objects.create(**userData)
        Token.objects.create(user=userInstance)
        validated_data['user'] = userInstance
        instance = Profile.objects.create(**validated_data)
        return instance

class PostalCodeSerializer(ModelSerializer):
    class Meta:
        model = PostalCode
        fields = ['postalCode', 'city', 'state', 'country']

class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ['username', 'startDate', 'endDate', 'streetAddress', 'postalCode', 'waiterNumber', 'score']

class EventAssistanceSerializer(ModelSerializer):
    class Meta:
        model = EventAssistance
        fields = ['event', 'username', 'accepted', 'score']

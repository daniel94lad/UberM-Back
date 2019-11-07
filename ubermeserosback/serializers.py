from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import Profile
from events.models import Event, EventAssistance
from postalcode.models import PostalCode

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class Base64ImageField(serializers.ImageField):

    def to_internal_value(self, data):
        from django.core.files.base import ContentFile
        import base64
        import six
        import uuid

        # Check if this is a base64 string
        if isinstance(data, six.string_types):
            # Check if the base64 string is in the "data:" format
            if 'data:' in data and ';base64,' in data:
                # Break out the header from the base64 content
                header, data = data.split(';base64,')

            # Try to decode the file. Return validation error if it fails.
            try:
                decoded_file = base64.b64decode(data)
            except TypeError:
                self.fail('invalid_image')

            # Generate file name:
            file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
            # Get the file name extension:
            file_extension = self.get_file_extension(file_name, decoded_file)

            complete_file_name = "%s.%s" % (file_name, file_extension, )

            data = ContentFile(decoded_file, name=complete_file_name)

        return super(Base64ImageField, self).to_internal_value(data)

    def get_file_extension(self, file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

class TokenSerializer(ModelSerializer):
    # user = UserSerializer()
    class Meta:
        model = Token
        fields = ['key']

class ProfileSerializer(ModelSerializer):
    user = UserSerializer()
    avatar = Base64ImageField(
        max_length=None, use_url=True,
    )
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

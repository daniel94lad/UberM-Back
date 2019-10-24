from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.http import Http404
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from ubermeserosback.serializers import TokenSerializer, UserSerializer, ProfileSerializer
from users.models import Profile

# Create your views here.
class UserLoginAuthenticationView(APIView):

    def get_user_object(self, username, password):
        try:
            user = User.objects.get(username=username)
            if check_password(password, user.password):
                return user
            else:
                raise User.DoesNotExist
        except User.DoesNotExist:
            raise Http404

    def get_token(self, username, password):
        user = self.get_user_object(username, password)
        try:
            token = Token.objects.get(user=user)
            serializer = TokenSerializer(token)
            return serializer.data
        except Token.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        requestUsername=request.GET.get('username')
        requestPassword=request.GET.get('password')
        token = self.get_token(requestUsername, requestPassword)
        return Response(token)

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class MeserosViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Profile.objects.filter(active=True)
    serializer_class = ProfileSerializer
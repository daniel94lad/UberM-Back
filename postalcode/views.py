from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from ubermeserosback.serializers import PostalCodeSerializer
from postalcode.models import PostalCode

class PostalCodeViewSet(ModelViewSet):
    queryset = PostalCode.objects.all()
    serializer_class = PostalCodeSerializer
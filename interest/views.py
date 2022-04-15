from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import InterestSerializer
from rest_framework import permissions

# Create your views here.
class AddInterest(CreateAPIView):
	permission_classes = (permissions.AllowAny)
	serializer_class = InterestSerializer

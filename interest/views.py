from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView
from .serializers import InterestSerializer
from rest_framework import permissions
from accounts.models import User
from .models import Interest

# Create your views here.
class AddInterest(CreateAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = InterestSerializer

class ListInterest(ListAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = InterestSerializer

class AddInterestToUser(CreateAPIView):
	permission_classes = (permissions.IsAuthenticated,)
	def post(self, request, id):
		email = request.user
		user = User.objects.get(email=email)
		interest = Interest.objects.get(id=id)
		user.interests.add


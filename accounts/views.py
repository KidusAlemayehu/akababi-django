from django.shortcuts import render
from .serializers import LoginSerializer, RegistrationSerializer, UserProfileSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User
from location.models import Location
from location.views import geolocator
import uuid

# Create your views here.
class SignUpAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "RequestID":str(uuid.uuid4()),
                "Message":"User Successfully Created",
                "User":serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginAPIView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

class UserProfileView(ListAPIView):
    def get(self, request, username):
        qs = User.objects.get(username=username)
        serializer = UserProfileSerializer(qs, many=False)
        return Response(serializer.data)

class UserProfileCreateView(CreateAPIView):
    serializer_class = UserProfileSerializer
    def post(self, request, username):
        qs = User.objects.get(username=username)
        serializer = self.get_serializer(qs, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileUpdateView(UpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = (permissions.IsAuthenticated,)
    def patch(self, request, username):
        user = User.objects.get(username=username)
        current_user = User.objects.get(email=request.user)
        if user.id != current_user.id:
            return Response(status=status.HTTP_403_UNAUTHORIZED)

        serializer = self.get_serializer(user, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            user.education = request.data.get("education", user.education)
            user.education = request.data.get("education", user.education)
            user.interests.set = request.data.get("interests", user.interests)
            user.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
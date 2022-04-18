from django.shortcuts import render
from .serializers import LoginSerializer, RegistrationSerializer, UserProfileSerializer
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView 
from .models import User
from location.models import Location
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
    def get(self, request, id):
        qs = User.objects.get(id=id)
        serializer = UserProfileSerializer(qs, many=False)
        return Response(serializer.data)
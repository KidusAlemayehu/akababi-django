from django.shortcuts import render
from .serializers import LoginSerializer, RegistrationSerializer, UserProfileSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from location.models import Location
from location.views import geolocator
from datetime import date, datetime
from django.contrib.sites.shortcuts import get_current_site
from .utils import Util
from django.urls import reverse
import uuid

# Create your views here.
class SignUpAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            bd = request.data.get("DOB")
            date_bd = datetime.strptime(bd, '%Y-%m-%d')
            today = date.today()
            age = today.year - date_bd.year
            if age >= 13:
                serializer.save()
                user_data = serializer.data
                user = User.objects.get(email=user_data['email'])
                token = RefreshToken.for_user(user).access_token
                current_site = get_current_site(request).domain
                relative_uri = reverse('verify_email')
                url = "http://"+current_site+relative_uri+"?token="+str(token)
                data = {'email_body':'Hi '+user.username+'please verify your account by using the link below \n'+url, 'to':user.email, 'email_subject':'Verify Your Email'}
                Util.send_email(data)
                return Response({
                    "RequestID":str(uuid.uuid4()),
                    "Message":"User Successfully Created",
                    "User":serializer.data}, status=status.HTTP_201_CREATED)
            elif age<13:
                return Response({"message":"under age"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserActivationView(GenericAPIView):
    def get(self,request):
        pass


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
        user = User.objects.get(username=username)
        serializer = self.get_serializer(user, data=request.data, many=False)
        if serializer.is_valid():
            user.interests.set= request.data.get("interests", user.interests)
            user.save()
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
            return Response({"message":"method not allowed"}, status=status.HTTP_401_UNAUTHORIZED)

        serializer = self.get_serializer(user, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            user.education = request.data.get("education", user.education)
            user.education = request.data.get("education", user.education)
            user.interests.set= request.data.get("interests", user.interests)
            user.save()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileDeleteView(DestroyAPIView):
    pass
from django.shortcuts import render
from .serializers import LoginSerializer, RegistrationSerializer, UserProfileSerializer
from rest_framework.generics import GenericAPIView,CreateAPIView, ListAPIView
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
        serializer = self.get_serializer(qs, many=False)
        return Response(serializer.data)

# class UserLocationCreateView(GenericAPIView):
#     # permission_classes = (permissions.IsAuthenticated,)
#     serializer_class = UserProfileSerializer
#     def patch(self, request, username):
#         user = User.objects.get(username=username)
#         data = request.data
#         address = data['address']
#         if Location.objects.get(name=address).exists():
#             location = Location.objects.get(name=address)
#             user.address =location.id
#         else:
#             location =  geolocator.geocode(address)
#             lat = location.latitude
#             lng = location.longitude
#             new_location = Location.objects.create(name=address, lat=lat, lng=lng)
#             new_location.save()
#             user.address = new_location.id

#         serializer = self.get_serializer_class(user, many=False)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({serializer.data}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
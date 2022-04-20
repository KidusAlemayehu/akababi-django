from rest_framework.generics import CreateAPIView
from geopy.geocoders import Nominatim
from accounts.models import User
from .serializers import LocationSerializer
from .models import Location
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
import uuid

geolocator = Nominatim(user_agent='akababi')
class UserLocationCreateView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LocationSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        name = request.data['name']
        if Location.objects.filter(name=name).exists():
            user = User.objects.get(email=request.user)
            user.address = Location.objects.get(name=name)
            user.save()
            return Response(status=201)
        elif serializer.is_valid():
            instance = serializer.save()
            location = geolocator.geocode(instance.name)
            print(location.latitude, location.longitude)
            instance.lat = location.latitude
            instance.lng = location.longitude
            user = User.objects.get(email=request.user)
            user.address = Location.objects.get(id=instance.id)
            user.save()
            instance.save()
            return Response({
                "RequestID":str(uuid.uuid4()),
                "Message":"Location Successfully Created",
                "Location":serializer.validated_data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
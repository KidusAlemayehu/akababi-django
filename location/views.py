from rest_framework.generics import CreateAPIView
from geopy.geocoders import Nominatim
from .serializers import LocationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
import uuid

geolocator = Nominatim(user_agent='akababi')
class LocationCreateView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LocationSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            location = geolocator.geocode(instance.name)
            print(location.latitude, location.longitude)
            instance.lat = location.latitude
            instance.lng = location.longitude
            instance.save()
            return Response({
                "RequestID":str(uuid.uuid4()),
                "Message":"Location Successfully Created",
                "Location":serializer.validated_data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
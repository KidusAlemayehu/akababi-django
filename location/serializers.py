from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id','name', 'lat', 'lng')
        extra_kwargs = {'id':{'read_only':True},'lat':{'read_only':True}, 'lng':{'read_only':True}}
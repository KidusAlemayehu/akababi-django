from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password
from interest.serializers import InterestSerializer
from location.serializers import LocationSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(max_length=250, min_length=6)
    gender = serializers.MultipleChoiceField(choices=(("Male", "Male"),("Female", "Female")))
    class Meta:
        model = User
        fields = (
            'full_name',
            'username',
            'email',
            'password',
            'gender',
            'DOB',
            'user_type',)
        extra_kwargs = {'password': {'write_only': True},
                        'user_type':{'write_only':True}}

    def validate_password(self, value):
        return make_password(value)


class LoginSerializer(TokenObtainPairSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.username

        return token

class UserProfileSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True, read_only=True)
    address = LocationSerializer(many=False, read_only=True)
    class Meta:
        model = User
        fields = ['id','full_name', 'username','email','gender','DOB','address','marital_status','occupation','education','experience','interests']
        extra_kwargs = {'id':{'read_only':True},'username':{'read_only':True},'full_name':{'read_only':True}, 'email':{'read_only':True}, 'gender':{'read_only':True},'DOB':{'read_only':True}}

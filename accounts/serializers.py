from .models import User, UserProfile
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password


class RegistrationSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(max_length=250)
    class Meta:
        model = User
        fields = (
            'full_name',
            'username',
            'email',
            'password',
            'gender',
            'DOB',
            'is_social',
            'is_work')
        extra_kwargs = {'password': {'write_only': True},
                        'is_social':{'write_only':True},'is_work': {'write_only': True}}

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
    class Meta:
        model = User
        fields = ('id','home_address','marital_status','work_address','occupation','education','experience','interests')
        extra_kwargs = {'id':{'read_only':True},}
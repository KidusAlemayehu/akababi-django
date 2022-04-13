from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from location.models import Location

class User(AbstractBaseUser):

    id = models.BigAutoField(primary_key=True, unique=True)
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=25, unique=True, default=None)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=350)
    gender = models.CharField(choices=[('male', 'Male'),('female', 'Female')], max_length=10)
    DOB = models.DateField()
    date_joined = models.DateField(auto_now=True)
    is_social = models.BooleanField(default=False)
    is_work = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = BaseUserManager()


class UserProfile(models.Model):
    id = models.BigAutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    address = models.ForeignKey(Location, null=True, on_delete=models.SET_NULL)
    marital_status = models.CharField(max_length=20, choices=(('single','Single'),('in relationship','In Relationship'),('engaged','Engaged'),('married','Married')), default=('single','Single'))
    experience = [models.JSONField(default={"start_date": None, "end_date": None, "Role": None, "Workplace": None})]
    education = [models.JSONField(default={"start_date": None, "end_date": None, "School": None})]
    occupation =  models.CharField(max_length=20, choices=(('student','Student'),('employed','Employed'),('self employed','Self Employed'),('unemployed','Unemployed'),('freelancer','Freelancer')))
    # social_interests = models.ManyToManyField(SocialInterest, default=None, null=True)
    # work_interests = models.ManyToManyField(WorkInterest, default=None, null=True)

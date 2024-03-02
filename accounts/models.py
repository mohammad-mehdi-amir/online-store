from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

class Customuser(AbstractUser):
    
    phone_number=PhoneNumberField(region='IR',null=True,blank=True)


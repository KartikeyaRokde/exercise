from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    """
    Custom user class.
    """
    # Registration information
    email = models.EmailField('email address', unique=True, db_index=True)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    
    # Geo-location information
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    
    # Defining the username field as email
    USERNAME_FIELD = 'email'
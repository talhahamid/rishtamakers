from django.db import models
from datetime import datetime, timedelta

# Create your models here. 
class User(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField(12,unique=True)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=200)
    state=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    religion=models.CharField(max_length=100)
    marital_status=models.CharField(max_length=100) 
    looking_for=models.CharField(max_length=100)
    
class Personal(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    education=models.CharField(max_length=100)
    occupation=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    mother_tongue=models.CharField(max_length=100)
    religion_category=models.CharField(max_length=100)
    cast_category=models.CharField(max_length=100)
    income=models.IntegerField(10)
    height=models.CharField(max_length=100)
    weight=models.IntegerField(10)
    color=models.CharField(max_length=100)

class Profilepic(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic1 = models.ImageField(upload_to='profile_pics/')
    profilepic2 = models.ImageField(upload_to='profile_pics/')    
    profilepic3 = models.ImageField(upload_to='profile_pics/')
    profilepic4 = models.ImageField(upload_to='profile_pics/')

class Subscribe(models.Model):    
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    plan=models.CharField(max_length=20,unique=True)
    duration=models.IntegerField(10)
    users=models.IntegerField(10)
    price=models.IntegerField(10)
    createdat=models.DateTimeField(auto_now_add=True)

class ProfileView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    viewed_profile = models.ForeignKey(User, related_name='viewed_profiles', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


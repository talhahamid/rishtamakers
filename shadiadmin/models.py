from django.db import models
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Demo(models.Model):
    name=models.CharField(max_length=100)


class Users(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField(12)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    address=models.CharField(max_length=200)
    dob=models.DateField()
    gender=models.CharField(max_length=100)
    religion=models.CharField(max_length=100)
    status=models.CharField(max_length=100) 
     

class Religion(models.Model): 
    name=models.CharField(max_length=100) 
 
class Religion_category(models.Model): 
    religion_name=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100)


class Status(models.Model):
    name=models.CharField(max_length=100)
   
class Education(models.Model): 
    name=models.CharField(max_length=100)

class Occupation(models.Model):
    occupation_name=models.CharField(max_length=100)
    sub_category=models.CharField(max_length=100) 
     
class Mothertongue(models.Model):
    name=models.CharField(max_length=100)
            
class Admin(models.Model):
    uid=models.CharField(max_length=100)
    password=models.CharField(max_length=100)


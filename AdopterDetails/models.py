from django.db import models

# Create your models here.
class AdopterDetailModel(models.Model):
    firstName = models.CharField(max_length=100,null=False)
    lastName = models.CharField(max_length=100,null=False)
    address1 = models.TextField(max_length=500,null=False)
    address2 = models.TextField(max_length=500,null=False)
    age      = models.PositiveIntegerField(null=False)
    ZipCode  = models.PositiveIntegerField(null=False)
    city  =    models.CharField(max_length=100,null=False)
    Email   = models.EmailField(max_length= 200, null= False)
    phone  = models.PositiveIntegerField(null=False)
    contactPref = models.CharField(null =  False , max_length= 100)
    aboutThem  = models.TextField(max_length=500,null=False)
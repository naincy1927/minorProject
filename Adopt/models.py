from django.db import models

# Create your models here.
class adoptModel(models.Model):
    a_type = models.CharField(max_length=50 , null=False)
    a_age =  models.IntegerField(null= False)
    a_gender =  models.CharField(max_length=50 , null= False) 
    a_color = models.CharField(max_length= 50, null = False)
    a_bread = models.CharField(max_length= 500)
    a_address = models.TextField(max_length=500 , null=False)
    vaccinated = models.CharField(max_length=100,null=False)
    a_img = models.FileField(upload_to= "jeeva/" , max_length= 500 , null=True )
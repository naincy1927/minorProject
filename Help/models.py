from django.db import models
class HelpModel(models.Model):
    category  = models.CharField(max_length=100,null=False)
    age       = models.PositiveIntegerField(null= False)
    gender    = models.CharField (max_length=10, null= False)
    location  = models.TextField(max_length=500,null=False)
    quantity  = models.PositiveIntegerField(null=False)
    userName  = models.CharField(max_length=100,null=False)
    userContact = models.PositiveIntegerField(null = False)
    userAddress  = models.TextField(max_length=500 , null = False)
    findingDate  = models.DateField(null=False)


 



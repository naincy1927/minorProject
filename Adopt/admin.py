from django.contrib import admin
from Adopt.models import adoptModel
# Register your models here.
class adoptAdmine(admin.ModelAdmin):
       list_display = ('id','a_type','a_gender','a_color','a_bread','a_address','a_img','vaccinated')
admin.site.register(adoptModel , adoptAdmine)
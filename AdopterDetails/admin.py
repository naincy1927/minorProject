from django.contrib import admin
from AdopterDetails.models import AdopterDetailModel
class AdopterAdmin(admin.ModelAdmin):
    list_display = ('id', 
    'firstName', 
    'lastName',
    'address1',
    'address2',
    'age',
    'ZipCode',
    'city',
    'Email',
    'phone',
    'contactPref',
    'aboutThem')

admin.site.register(AdopterDetailModel,AdopterAdmin)

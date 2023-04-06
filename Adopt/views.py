from django.shortcuts import render , HttpResponse
from Adopt.models import adoptModel
def AdoptPage(request):
    contex = adoptModel.objects.all()
    data = {
        'contex':contex
    }    
    return render(request , "adopt.html",data)

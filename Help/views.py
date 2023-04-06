from django.shortcuts import render
from Help.models import HelpModel
def helpPage(request):
      # x = HelpModel
      if request.method == "POST":

        # x = HelpModel

        z = request.POST.get('name')
        z1 = request.POST.get('age')
        z2 = request.POST.get('gender')
        z3 = request.POST.get('location')
        z4 = request.POST.get('num')
        z5 = request.POST.get('uName')
        z6 = request.POST.get('cn')
        z7 = request.POST.get('address')
        z8 = request.POST.get('fdate')
        
        
        data2 = HelpModel(  category    = z,
        age         = z1,
        gender      = z2,
        location    = z3,
        quantity    = z4,
        userName    = z5,
        userContact = z6,
        userAddress  = z7,
        findingDate  = z8,)

        data2.save()  
        return render(request , 'help.html')
      else:
          return render(request,'help.html')


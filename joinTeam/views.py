from django.shortcuts import render , HttpResponse
from joinTeam.models import myModel
def joinPage(request):

      if request.method == "POST":

        # x = myModel()

        name = request.POST.get('name')
        eadress = request.POST.get('eaddress')
        phone = request.POST.get('phone')
        wn = request.POST.get('wn')
        age = request.POST.get('age')
        city = request.POST.get('city')
        zip1 = request.POST.get('zip1')
        info = request.POST.get('info')
        aleargy = request.POST.get('aleargy')
        day = request.POST.get('day')
        activity = request.POST.get('activity')
        visit= request.POST.get('visit')
    
        x = myModel(
        Name = name,
        email = eadress,
        phone = phone,
        wattsapp = wn,
        age = age,
        city = city,
        zipCode = zip1,
        contactShare = info,
        Allergy = aleargy,
        daysAttending = day,
        activities = activity,
        about = visit)

        x.save()
        #  messages.success(request , 'data is saved')    
        return render (request , 'volunteer.html')
      else:
        return render(request , 'volunteer.html')
      

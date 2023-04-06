from django.shortcuts import render
from AdopterDetails.models import AdopterDetailModel
def userPage(request):
      if request.method == "POST":
            # y=AdopterDetailModel
            m = request.POST.get('fname')
            m1 = request.POST.get('lname')
            m2 = request.POST.get('address1')
            m3 = request.POST.get('address2')
            m4 = request.POST.get('age')
            m5 = request.POST.get('zip1')
            m6 = request.POST.get('city')
            m7 = request.POST.get('eaddress')
            m8 = request.POST.get('phone')
            m9 = request.POST.get('contact')
            m10 = request.POST.get('visit')


            data1 = AdopterDetailModel( firstName = m,
            lastName  = m1,
            address1  = m2,
            address2  = m3,
            age       = m4,
            ZipCode   = m5,
            city      = m6,
            Email     = m7,
            phone     = m8,
            contactPref = m9,
            aboutThem   = m10
            )

            data1.save()
            return render (request , 'adoptdetail.html')
      else:
            return render (request , 'adoptdetail.html')


from django.contrib import admin

# Register your models here.
from joinTeam.models import myModel
# Register your models here.
class myAdmine(admin.ModelAdmin):
    list_display = [
            'id',
            'Name',
            'email',
            'phone',
            'wattsapp',
            'age',
            'city',
            # 'zipCode',
            # 'contactShare',
            # 'Allergy',
            # 'daysAttending',
            # 'activities',
            # 'about'
    ]
    list_display_links = ['Name','id']
    # radio_fields = {"contactShare":admin.HORIZONTAL, "daysAttending":admin.HORIZONTAL,"activities":admin.HORIZONTAL}
    # list_display_links = ['Name','id']
    # list_filter = ['Name','Allergy','daysAttending','activities','city','zipCode']
    # def _(self,obj):
    #     if obj.Situation =="Read":
    #         return True
    #     else:
    #         return False
    # _.boolean = True
    
    # def status (self,obj)


          
   
admin.site.register(myModel,myAdmine)
from django.contrib import admin
from Help.models import HelpModel
class HelpAdmine(admin.ModelAdmin):
    list_display = ('id',
                    'category',
                    'age',
                    'gender',
                    'location',
                    'quantity',
                    'userName',
                    'userContact',
                    'userAddress',
                    'findingDate'
                    )
admin.site.register(HelpModel,HelpAdmine)


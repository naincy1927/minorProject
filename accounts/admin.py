from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
class accountAdmin(UserAdmin):
    list_display = ('id','email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links = ('email','id','first_name','last_name')
    readonly_fields  = ('last_login','date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter  = ()
    fieldsets = ()


admin.site.register(Account,accountAdmin)

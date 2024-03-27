from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customuser
from django.utils.translation import gettext as _
# Register your models here.

@admin.register(Customuser)
class CustomuserAdmin(UserAdmin):
    list_display =['email','username','phone_number']
    
    fieldsets =  (
        (_('Custom Fields'), {
            'fields': ('phone_number',)
        }),
    )+UserAdmin.fieldsets 

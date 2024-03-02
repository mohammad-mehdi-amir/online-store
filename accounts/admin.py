from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Customuser
# Register your models here.

@admin.register(Customuser)
class CustomuserAdmin(UserAdmin):
    pass

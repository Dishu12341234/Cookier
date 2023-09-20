from django.contrib import admin
from .models import AppUser
# Register your models here.
class AppUserModel(admin.ModelAdmin):
    list_display = ('username','email','gender')

admin.site.register(AppUser,AppUserModel)
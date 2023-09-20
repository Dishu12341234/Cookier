from django.contrib import admin
from .models import AppUser,FoodItems
# Register your models here.
class AppUserModel(admin.ModelAdmin):
    list_display = ('username','email','gender')
class FoodModel(admin.ModelAdmin):
    list_display = ('itemname','price','username','itemtype')
admin.site.register(AppUser,AppUserModel)
admin.site.register(FoodItems,FoodModel)
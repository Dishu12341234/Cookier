from django.contrib import admin
from .models import AppUser,FoodItems, ItemLogs
# Register your models here.
class AppUserModel(admin.ModelAdmin):
    list_display = ('username','email','gender')
class FoodModel(admin.ModelAdmin):
    list_display = ('itemname','price','username','itemtype')
class ItemModel(admin.ModelAdmin):
    list_display = ('itemname','username','amount')
admin.site.register(AppUser,AppUserModel)
admin.site.register(FoodItems,FoodModel)
admin.site.register(ItemLogs)
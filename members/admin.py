from django.contrib import admin
from .models import AppUser,FoodItems, Cart,Orders
# Register your models here.
class AppUserModel(admin.ModelAdmin):
    list_display = ('username','email','gender')
class FoodModel(admin.ModelAdmin):
    list_display = ('itemname','price','username','itemtype')
class CartModel(admin.ModelAdmin):
    list_display = ('itemname','amount','username')
class OrderModel(admin.ModelAdmin):
    list_display = ('username','date')
admin.site.register(AppUser,AppUserModel)
admin.site.register(FoodItems,FoodModel)
admin.site.register(Cart,CartModel)
admin.site.register(Orders,OrderModel)
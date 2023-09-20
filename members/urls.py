from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('Login/',views.login_user,name='login'),
    path('Logout/',views.logout_user,name='logout'),
    path('Cart/',views.cart,name='cart'),
    path('Orders/',views.orders,name='orders'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('Signin/',views.signin_user,name='signin'),
    path('Login/',views.login_user,name='login'),
    path('Logout/',views.logout_user,name='logout'),
    path('Cart/',views.cart,name='cart'),
    path('Orders/',views.orders,name='orders'),
    path('AddItem/',views.add_item,name='ai'),
    path('GetItem/<str:iname>',views.get_item,name='gi'),
]
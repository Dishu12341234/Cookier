from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('Signin/',views.signin_user,name='signin'),
    path('Login/',views.login_user,name='login'),
    path('Logout/',views.logout_user,name='logout'),
    path('Cart/<str:itemname>/<str:amount>/<str:price>',views.cart,name='cart'),
    path('Cart/',views.cart,name='cart'),
    path('Orders/',views.orders,name='orders'),
    path('AddItem/',views.add_item,name='ai'),
    path('GetItem/<str:iname>/<str:uname>',views.get_item,name='gi'),
    path('ChangeItem/<str:iname>',views.change_item,name='ci'),
    path('Order/<str:tp>/<str:items>',views.order,name='order'),
]
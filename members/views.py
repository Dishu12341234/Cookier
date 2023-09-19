from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render,redirect
# Create your views here.
def index(req):
    return render(req,"index.html",{})
def login(req):
    return render(req,'login.html',{})
def logout(req):
    return render(req,'logout.html',{})
def cart(req):
    return render(req,'cart.html',{})
def orders(req):
    return render(req,'orders.html',{})
def custom_404_view(request, exception=None):
    return render(request, '404.html')
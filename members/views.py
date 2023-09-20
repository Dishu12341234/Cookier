from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import SignUpForm
from .models import AppUser
# Create your views here.


def index(req):
    return render(req, "index.html", {})


def login_user(req):
    if req.method == 'POST':
        uname = req.POST. get('username')
        email = req.POST.get('email')
        pass1 = req.POST.get('password')
        fname = req.POST.get('first_name')
        lname = req.POST.get('last_name')
        gender = req.POST.get('gender')
        area = req.POST.get('area')
        phone_number = req.POST.get('phone_number')
        user = User.objects.create_user(
            username=uname, password=pass1, email=email, first_name=fname, last_name=lname)
        user.save()
        app_user = AppUser.objects.create(
            username=uname,
            email=email,
            password=pass1,  # Note: You should use a secure password hashing method
            first_name=fname,
            last_name=lname,
            gender=gender,
            area=area,
            phone_number=phone_number
        )
        app_user.save()
        login(req, user)
        return redirect('/')
    return render(req, 'login.html', {'form': SignUpForm()})

    return render(req, 'login.html', {})


def logout_user(req):
    logout(req)
    return render(req, 'logout.html', {})


def cart(req):
    return render(req, 'cart.html', {})


def orders(req):
    return render(req, 'orders.html', {})


def custom_404_view(request, exception=None):
    return render(request, '404.html')

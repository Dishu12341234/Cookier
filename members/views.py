from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from .forms import AddItemForm, ChangeItemForm, SignUpForm,LoginForm
from .models import AppUser, FoodItems, ItemLogs
from django.contrib.auth.hashers import check_password
# Create your views here.


def index(req):
    print(req.user.username)
    user_is_admin = User.objects.filter(is_staff = True,username = req.user.username).values().exists()#If the user is staff or not
    items = FoodItems.objects.all().values()
    return render(req, "index.html", {'admin':user_is_admin,'items':items})


def signin_user(req):
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
            password=user.password,  # Note: You should use a secure password hashing method
            first_name=fname,
            last_name=lname,
            gender=gender,
            area=area,
            phone_number=phone_number
        )
        app_user.save()
        login(req, user)
        return redirect('/')
    return render(req, 'signin.html', {'form': SignUpForm()})

def login_user(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = User.objects.get(username=username)
        checked_password = check_password(password,user.password)
        if checked_password:
            login(req,user)
            return redirect('/')
    return render(req,'login.html',{'form':LoginForm()})


def logout_user(req):
    logout(req)
    return render(req, 'logout.html', {})


def cart(req):
    return render(req, 'cart.html', {})


def orders(req):
    return render(req, 'orders.html', {})

def add_item(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            username = req.user.username
            itemname = req.POST.get('itemname')
            price = req.POST.get('price')
            description = req.POST.get('description')
            ingridents = req.POST.get('ingridents')
            itemtype = req.POST.get('itemtype')
            item = FoodItems(username=username,itemname=itemname,price=price,description=description,ingridents=ingridents,itemtype=itemtype)
            item.save()
            return redirect('/')

        return render(req,'add_item.html',{'form':AddItemForm()})
    return redirect('/Login')

def custom_404_view(request, exception=None):
    return render(request, '404.html')

def get_item(req,iname):
    item = FoodItems.objects.get(itemname=iname)
    print(item)
    return render(req,'item.html',{'item':item})

def change_item(req,iname):
    if req.user.is_authenticated:
        if req.method == 'POST':
            username = req.user.username
            itemname = req.POST.get('itemname')
            newitemname = req.POST.get('newitemname')
            price = req.POST.get('price')
            description = req.POST.get('description')
            ingridents = req.POST.get('ingridents')
            itemtype = req.POST.get('itemtype')

            item = FoodItems.objects.get(itemname=itemname)
            item.username = username
            item.itemname = newitemname
            item.price = price
            item.description = description
            item.ingridents = ingridents
            item.itemtype = itemtype
            item.save()
            return redirect('/')

        return render(req,'add_item.html',{'form':ChangeItemForm()})
    return redirect('/Login')
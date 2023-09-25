from django.contrib.auth.models import User
from django import forms
from .models import AppUser,FoodItems,Orders

class SignUpForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['username','email','password','first_name','last_name','area','phone_number','gender']

class AddItemForm(forms.ModelForm):
    class Meta:
        model = FoodItems
        fields = ['username','itemname','price','description','ingridents','itemtype']
class ChangeItemForm(AddItemForm):
    newitemname = forms.CharField(max_length=50)
    class Meta:
        model = FoodItems
        fields = AddItemForm.Meta.fields

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150,required=True)
    password = forms.CharField(max_length=128,required=True)
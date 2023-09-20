from django.contrib.auth.models import User
from django import forms
from .models import AppUser

class SignUpForm(forms.ModelForm):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = forms.ChoiceField(
            choices=GENDER_CHOICES,
            widget=forms.Select(attrs={'class': 'form-control'}),
            required=True,
            label='Gender',
        )
    class Meta:
        model = AppUser
        fields = ['username','email','password','first_name','last_name','area','phone_number']
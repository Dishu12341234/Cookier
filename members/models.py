from django.db import models
import json

# Create your models here.
class AppUser(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # You should use a secure password storage method.
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    GENDER_CHOICES = [
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other'),
    ]

    area = models.TextField(max_length=100,unique=False,default='Select City')
    phone_number = models.CharField(max_length=13)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='M')


    def __str__(self):
        return self.username
    
class FoodItems(models.Model):
    username = models.CharField(max_length=150)
    itemname = models.CharField( max_length=50,unique=True)
    price = models.CharField(max_length=4)
    description = models.CharField(max_length=300)
    ingridents = models.CharField(max_length=300)
    itemtype = models.CharField(max_length=200)
    def __str__(self):
        return self.itemname + ' ---->  ' + self.username
    

class Cart(models.Model):
    username = models.CharField(max_length=150)
    itemname = models.CharField( max_length=50,unique=True)
    price = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    
    def __str__(self):
        return self.itemname + ' ---->  ' + f'{self.amount}'
    

class Orders(models.Model):
    username = models.CharField(max_length=150)
    totalPrice = models.BigIntegerField(default=0)
    items = models.TextField(null=False,blank=False)#Store JSON Data only
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.username + ' for ' + f'Rs{self.totalPrice}' + ' at ' + f'{self.date}'
from django.db import models

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
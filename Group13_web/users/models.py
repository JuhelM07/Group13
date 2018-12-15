from django.db import models
from django import forms
from django.contrib.auth.models import User
from users.choices import *
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    birth_date = models.DateField()
    hobbies = MultiSelectField(choices=HOBBY_CHOICES)

    def __str__(self):
        return f'{self.user.username} Profile'

class Matches(models.Model):
    usernames = User.objects.values_list('username', flat=True)

    def __str__(self):
        return f'{self.users.username} Matches'

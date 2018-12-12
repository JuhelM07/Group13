from django.db import models
from django import forms
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    GENDER_CHOICES = (
           ("M", "Male"),
           ("F", "Female"),
           ("O", "Other")
      )
    gender = forms.ChoiceField(choices = GENDER_CHOICES)
    birth_date = models.DateField()

    def __str__(self):
        return f'{self.user.username} Profile'

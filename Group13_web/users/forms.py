from django import forms
import datetime
from dobwidget import DateOfBirthWidget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from users.choices import *

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    gender = forms.ChoiceField(widget=forms.Select(), choices=GENDER_CHOICES, required=True)
    hobbies = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=HOBBY_CHOICES, required=True)
    birth_date= forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'hobbies', 'birth_date']

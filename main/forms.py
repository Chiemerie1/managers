from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import MainManager



class RegistrationForm(UserCreationForm):
    class Meta:
        model = MainManager
        fields = ["enterprise_name", "first_name", "last_name", "email", "password1", "password2"]



class LoginForm(forms.Form):
    enterprise_name = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    
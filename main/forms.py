from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import CustomUser



class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["enterprise_name", "first_name", "last_name", "email", "password1", "password2"]



class LoginForm(forms.Form):
    pass
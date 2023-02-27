from django import forms
from django.contrib.auth.forms import UserCreationForm

from main.models import CustomUser



class RegistrationForm(UserCreationForm):
    
    # enterprise_name = forms.CharField(
    #     max_length=200, required=True,
    #     help_text="Enter the name of your company"
    # )
    class Meta:
        model = CustomUser
        fields = ["enterprise_name", "first_name", "last_name", "email", "password1", "password2"]

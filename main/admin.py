from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.utils import timezone

from main.models import CustomUser

# Register your models here.


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ("enterprise_name","first_name", "last_name", "email")

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords does not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



class UserChangeForm(forms.ModelForm):
    
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "is_active", "date", "is_admin")


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["enterprise_name","first_name", "last_name", "email", "is_admin"]
    list_filter = ["is_admin"]

    fieldsets = (
        ("Login", {"fields": ("enterprise_name", "password", "date")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_admin",)}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide", ),
            "fields": (
                "enterprise_name",
                "first_name",
                "last_name",
                "email",
                "password",
                "password2"
            )
        }
        ),
    )

    search_fields = ("enterprise_name",)
    ordering = ("enterprise_name",)
    filter_horizontal = ()


admin.site.register(CustomUser, UserAdmin)
admin.site.unregister(Group)
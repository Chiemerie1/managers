from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from main.models import MainManager, FranchiseManager, ProductCategories, Products

# Register your models here.


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = MainManager
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
        model = MainManager
        fields = ("first_name", "last_name", "email", "is_active", "date", "is_admin")




class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["enterprise_name","first_name", "last_name", "email", "is_admin"]
    list_filter = ["is_admin"]

    fieldsets = (
        ("Login", {"fields": ("enterprise_name", "password", "date")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_admin", "is_active")}),
    )

    add_fieldsets = (
        ("User Creation", {
            "classes": ("wide", ),
            "fields": (
                "enterprise_name",
                "first_name",
                "last_name",
                "email",
                "password1",
                "password2"
            )
        }
        ),
    )

    search_fields = ("enterprise_name",)
    ordering = ("enterprise_name",)
    filter_horizontal = ()


# Model Admin fields

class ManagerAdmin(admin.ModelAdmin):

    list_display = ("first_name", "designation", "company")



class CategoryAdmin(admin.ModelAdmin):

    list_display = ["manager", "name"]
    search_fields = ["manager__first_name"]



class productAdmin(admin.ModelAdmin):

    list_display = ["item", "category", "unit_price", "stock", "total_price"]





admin.site.register(ProductCategories, CategoryAdmin)

admin.site.register(MainManager, UserAdmin)
admin.site.register(FranchiseManager, ManagerAdmin)
admin.site.register(Products, productAdmin)

admin.site.unregister(Group)


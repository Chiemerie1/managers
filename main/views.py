from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def registration(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            enterprise_name = form.cleaned_data.get("enterprise_name")
            password = form.cleaned_data.get("password1")
            user_account = authenticate(username=enterprise_name, password=password)
            login(request, user_account)
            return redirect("console")
        else:
            context["reg_form"] = form
    else:
        form = RegistrationForm()
        context["reg_form"] = form
    return render(request=request, template_name="main/register.html", context=context)


def console(request):
    context = {}
    return render(request, template_name="main/console.html")

def log_in(request):
    context ={}
    if request.method == "POST":
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            pass


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from main.forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# Registration
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
            return redirect("main:console")
        else:
            context["reg_form"] = form
    else:
        form = RegistrationForm()
        context["reg_form"] = form
    return render(request=request, template_name="main/register.html", context=context)


# console
@login_required #takes the following arguments (redirect_field_name, login_url)
def console(request):
    return render(request, template_name="main/console.html")


# login
def log_in(request):
    context ={}
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            enterprise_name = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=enterprise_name, password=password)
            if user.is_authenticated:
                login(request, user)
                return redirect("main:console")
        else:
            context["login_form"] = form
    else:
        form = AuthenticationForm()
        context["login_form"] = form
    return render(request, "main/log_in.html", context)
        


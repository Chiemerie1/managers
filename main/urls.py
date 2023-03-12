from django.urls import path
from main import views




app_name = "main"



urlpatterns = [
    path("", views.registration, name="register" ),
    path("console/", views.console, name="console"),
    path("log_in/", views.log_in, name="log_in"),
]

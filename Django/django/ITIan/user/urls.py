from django.urls import path
from user.views import LoginView, RegisterView


urlpatterns = [
    path("login", LoginView, name="user_login"),
    path("register", RegisterView, name="user_register"),
]

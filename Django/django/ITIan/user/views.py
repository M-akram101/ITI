from django.http import HttpResponse
from django.shortcuts import render


user = [
    {"id": 1, "username": "Akram", "password": "123456"},
    {"id": 2, "username": "Omar", "password": "123456"},
    {"id": 3, "username": "Ahmed", "password": "123456"},
]


# Create your views here.
def LoginView(request):
    obj = HttpResponse("<h1> hi django </h1>")
    obj.write("<h2> Second write</h2>")
    obj["content-type"] = "text/plain"  # dont parse Html code
    return obj


def logout(request):
    return HttpResponse("loggedout")


def RegisterView(requestobj):
    return render(requestobj, template_name="register.html")

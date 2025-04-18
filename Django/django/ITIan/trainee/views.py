# from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Trainee
from .forms import TraineeForm


def get_all_trainees(request):
    trainees = Trainee.objects.all()
    print("POSTiiiiing")

    return render(request, "trainee/list.html", {"trainees": trainees})


def create_trainee(request):
    print("Tesssssssssssssst")
    if request.method == "POST":

        print("koooooooooooooooo")
        form = TraineeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_all_trainees")
    else:
        form = TraineeForm()

    return render(request, "trainee/form.html", {"form": form})


def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)

    if request.method == "POST":
        form = TraineeForm(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect("get_all_trainees")
    else:
        form = TraineeForm(instance=trainee)

    return render(request, "trainee/form.html", {"form": form})


def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect("get_all_trainees")

# # Create your views here.
# from django.http import HttpResponse
# from django.shortcuts import render

# trainees = [
#     {"id": 1, "name": "Mohamed", "course": "Nodejs"},
#     {"id": 2, "name": "Akram", "course": "Python"},
#     {"id": 3, "name": "Aly", "course": "Java"},
# ]


# def get_course(request):
#     # res = HttpResponse(trainees)
#     # return res
#     return render(request, template_name="course.html")


# def get_all_courses(request):
#     courses = [[1, "cs50"], [2, "OS"], [3, "assembly"]]
#     # res = HttpResponse(trainees)
#     # return res
#     return render(
#         request,
#         template_name="course/all.html",
#         context={"coursedata": courses},
#     )


# def update_course(request, id):
#     res = HttpResponse(f"<h1 style='color:red'>Update trainee by id</h1> ${id}")
#     return res


# def delete_course(request):
#     res = HttpResponse("delete Section")
#     return res


# # Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from trainee.forms import TraineeForm
from trainee.models import Trainee
from .forms import CourseForm
from .models import Course


def course_list(request):
    courses = Course.objects.all()
    return render(request, "course/list.html", {"courses": courses})


def course_create(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm()
    return render(request, "course/form.html", {"form": form})


def course_update(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("course_list")
    else:
        form = CourseForm(instance=course)
    return render(request, "course/form.html", {"form": form})


def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect("course_list")

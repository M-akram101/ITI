from django.urls import path
from course.views import course_list, course_create, course_update, course_delete


urlpatterns = [
    path("", course_list, name="course_list"),
    path("create/", course_create, name="course_create"),
    path("update/<int:id>/", course_update, name="course_update"),
    path("delete/<int:id>/", course_delete, name="course_delete"),
]

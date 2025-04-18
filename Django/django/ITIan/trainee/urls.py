from django.urls import path
from .views import get_all_trainees, create_trainee, update_trainee, delete_trainee

urlpatterns = [
    path("", get_all_trainees, name="get_all_trainees"),
    path("create/", create_trainee, name="create_trainee"),
    path("update/<int:id>/", update_trainee, name="update_trainee"),
    path("delete/<int:id>/", delete_trainee, name="delete_trainee"),
]

from django.urls import path
from .views import TraineeDetailView, TraineeCreateUpdateView

urlpatterns = [
    path("<int:pk>/", TraineeDetailView.as_view(), name="trainee-detail"),
    path("", TraineeCreateUpdateView.as_view(), name="trainee-create"),
    path(
        "update/<int:pk>/",
        TraineeCreateUpdateView.as_view(),
        name="trainee-update",
    ),
]

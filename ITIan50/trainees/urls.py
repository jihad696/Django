from django.urls import path
from .views import *
  
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", login_required(TraineeListView.as_view()), name="trainee-list"),
    path("add/", login_required(TraineeCreateView.as_view()), name="trainee-add"),
    path(
        "update/<int:pk>/",
        login_required(TraineeUpdateView.as_view()),
        name="trainee-update",
    ),
    path(
        "delete/<int:pk>/",
        login_required(TraineeDeleteView.as_view()),
        name="trainee-delete",
    ),
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path(
        "api/trainees/",
        TraineeListCreateAPIView.as_view(),
        name="api-trainee-list-create",
    ),
    path(
        "api/trainees/<int:pk>/",
        TraineeRetrieveUpdateDestroyAPIView.as_view(),
        name="api-trainee-detail",
    ),
]

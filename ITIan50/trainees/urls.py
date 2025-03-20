from django.urls import path
from .views import TraineeListView, TraineeCreateView

urlpatterns = [
    path('', TraineeListView.as_view(), name='trainee-list'),
    path('add/', TraineeCreateView.as_view(), name='trainee-add'),
]
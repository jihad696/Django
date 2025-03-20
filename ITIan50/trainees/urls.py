from django.urls import path
from .views import TraineeListView, TraineeCreateView, TraineeUpdateView, TraineeDeleteView

urlpatterns = [
    path('', TraineeListView.as_view(), name='trainee-list'),
    path('add/', TraineeCreateView.as_view(), name='trainee-add'),
    path('update/<int:pk>/', TraineeUpdateView.as_view(), name='trainee-update'),
    path('delete/<int:pk>/', TraineeDeleteView.as_view(), name='trainee-delete'),
]
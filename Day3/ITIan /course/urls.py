from django.urls import path
from .views import *

urlpatterns = [
    path('list/', course_list, name='course_list'),  
    path('add/', add_course, name='add_course'),
    path('update/<int:pk>/', updatecourses, name='update_course'),
    path('delete/<int:course_pk>/', delete_course, name='delete_course'),
]

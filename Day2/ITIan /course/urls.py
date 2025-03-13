from django.urls import path
from .views import *

urlpatterns = [
    path('list/', course_list, name='course_list'),  
    path('add/', add_course, name='add_course'),
    path('update/<int:id>/', updatecourses, name='update_course'),
    path('delete/<int:course_id>/', delete_course, name='delete_course'),
]

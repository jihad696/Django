from django.shortcuts import render, redirect
from .models import Course
from .forms import CourseForm

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()

    return render(request, 'course/add_course.html', {'form': form})


def updatecourses(request, pk):
    course = Course.objects.get(id=pk)  
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)

    return render(request, 'course/update_course.html', {'form': form})


def course_list(request):
    active_course = Course.objects.all()
    return render(request, 'course/course_list.html', {'courses': active_course})


def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect('course_list')

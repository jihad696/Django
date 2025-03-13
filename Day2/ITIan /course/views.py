from django.shortcuts import render, redirect
from .models import Course

# Create your views here.

def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        new_course = Course(name=name, email=email, phone=phone)
        new_course.save()
        return redirect('course_list')
    return render(request, 'course/add_course.html')


def updatecourses(request, id):
    course = Course.objects.get(id=id)  
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        
        course.name = name
        course.email = email
        course.phone = phone
        course.save()
        return redirect('course_list')

    return render(request, 'course/update_course.html', {'course': course})


def course_list(request):
    active_course = Course.objects.filter(deleted=False)
    deleted_course = Course.objects.filter(deleted=True)
    return render(request, 'course/course_list.html', {
        'courses': active_course,
        'deleted_courses': deleted_course
    })


def delete_course(request, course_id):
    course = Course.objects.get(id=course_id)
    course.deleted = True
    course.save()
    return redirect('course_list')


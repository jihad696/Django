from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee

def trainee_list(request):
    trainees = Trainee.get_trainees()
    return render(request, 'trainee/list_trainee.html', {'trainees': trainees})


def add_trainee(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        course_id = request.POST.get('course')  
        image = request.FILES.get('image')

        if name and email and course_id:
            Trainee.objects.create(name=name, email=email, phone=phone, course_id=course_id, image=image)
            return redirect('trainee/list_trainee.html')

    return render(request, 'trainee/add_trainee.html')




def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)

    if request.method == 'POST':
        trainee.name = request.POST.get('name')
        trainee.email = request.POST.get('email')
        trainee.phone = request.POST.get('phone')
        trainee.course_id = request.POST.get('course')
        
        if 'image' in request.FILES:
            trainee.image = request.FILES['image']

        trainee.save()
        return redirect('trainee/list_trainee.html')

    return render(request, 'trainee/update_trainee.html', {'trainee': trainee})



def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee/list_trainee.html')

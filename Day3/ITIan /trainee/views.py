from django.shortcuts import render, redirect, get_object_or_404
from .models import Trainee
from .forms import TraineeForm

def trainee_list(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list_trainee.html', {'trainees': trainees})


def add_trainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            Trainee.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                phone=form.cleaned_data.get('phone', ''),
                course=form.cleaned_data['course'],
                image=form.cleaned_data.get('image', None)
            )
            return redirect('trainee_list')

    else:
        form = TraineeForm()

    return render(request, 'trainee/add_trainee.html', {'form': form})


def update_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)

    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)
        if form.is_valid():
            trainee.name = form.cleaned_data['name']
            trainee.email = form.cleaned_data['email']
            trainee.phone = form.cleaned_data.get('phone', '')
            trainee.course = form.cleaned_data['course']
            
            if form.cleaned_data['image']:
                trainee.image = form.cleaned_data['image']
            
            trainee.save()
            return redirect('trainee_list')

    else:
        form = TraineeForm(initial={
            'name': trainee.name,
            'email': trainee.email,
            'phone': trainee.phone,
            'course': trainee.course,
            'image': trainee.image
        })

    return render(request, 'trainee/update_trainee.html', {'form': form, 'trainee': trainee})


def delete_trainee(request, id):
    trainee = get_object_or_404(Trainee, id=id)
    trainee.delete()
    return redirect('trainee_list')

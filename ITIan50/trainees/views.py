from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Trainee
from .forms import UserRegisterForm


class TraineeListView(ListView):
    model = Trainee
    template_name = "trainees/trainee_list.html"


class TraineeCreateView(CreateView):
    model = Trainee
    template_name = "trainees/trainee_form.html"
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("trainee-list")


class TraineeUpdateView(UpdateView):
    model = Trainee
    template_name = "trainees/trainee_form.html"
    fields = ["first_name", "last_name", "email"]
    success_url = reverse_lazy("trainee-list")


class TraineeDeleteView(DeleteView):
    model = Trainee
    template_name = "trainees/trainee_confirm_delete.html"
    success_url = reverse_lazy("trainee-list")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("trainee-list")
    else:
        form = UserRegisterForm()
    return render(request, "trainees/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("trainee-list")
    else:
        form = AuthenticationForm()
    return render(request, "trainees/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")

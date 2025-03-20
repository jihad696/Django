from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Trainee


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

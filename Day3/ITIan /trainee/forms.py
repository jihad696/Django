from django import forms
from course.models import Course
class Traineeform (forms.Form):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    course = forms.ModelChoiceField(queryset=Course.objects.all())
    image = forms.ImageField(required=False)
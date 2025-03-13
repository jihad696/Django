from django import forms
from .models import Course
class Courseform(forms.ModelForm):
    class Meta :
        model = Course
        fields =['name' , 'description']
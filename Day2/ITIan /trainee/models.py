from django.db import models
from course.models import Course

# Create your models here.



class Trainee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="trainees")
    image = models.ImageField(upload_to='trainees/', null=True, blank=True)

    
    @classmethod
    def get_trainees(cls):
        return cls.objects.all()

    


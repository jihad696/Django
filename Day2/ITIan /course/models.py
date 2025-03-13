from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='course/images' , null=True)
    deleted = models.BooleanField(default=False) 
 





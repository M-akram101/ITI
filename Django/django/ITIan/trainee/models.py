from django.db import models

from course.models import Course


# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True)
    createdAt = models.DateField(auto_now_add=True)
    isActive = models.BooleanField(default=True)
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)

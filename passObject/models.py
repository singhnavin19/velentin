from django.db import models
# Create your models here.
class Student(models.Model):
    id:models.CharField(max_length=100)
    Fname:models.CharField(max_length=100)
    Lname:models.CharField(max_length=100)
    knowDjango:models.BooleanField(default=False)

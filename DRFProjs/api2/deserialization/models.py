from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    classs = models.IntegerField()
    section = models.CharField(max_length=1)
    roll = models.IntegerField()
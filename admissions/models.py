from django.db import models
from django import forms


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    fathername = models.CharField(max_length=255)
    classname = models.IntegerField()
    contact = models.CharField(max_length=255)


from django.db import models
from django import forms
from django.urls import reverse


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    fathername = models.CharField(max_length=255)
    classname = models.IntegerField()
    contact = models.CharField(max_length=255)


class Teacher(models.Model):
    name = models.CharField(max_length=255)
    experience = models.IntegerField()
    subject = models.CharField(max_length=255)
    contact = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('teacherlisturl')

from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# function based views

def homepage(request):
    return render(request, 'index.html')


def admission(request):
    # return HttpResponse("This is admission view")
    return render(request, 'admissions/add-admission.html', {'name': 'Saikiran', 'greeting': 'Welcome'})


def admission_report(request):
    # return HttpResponse("<h1>This is admission report view.</h1>")
    return render(request, 'admissions/admissions-report.html')

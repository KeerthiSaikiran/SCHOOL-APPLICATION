from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admission(request):
    # return HttpResponse("This is admission view")
    return render(request, 'admissions/add-admission.html')

def admission_report(request):
    # return HttpResponse("<h1>This is admission report view.</h1>")
    return render(request, 'admissions/admissions-report.html')
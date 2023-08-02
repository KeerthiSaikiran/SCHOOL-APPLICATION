from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def admission(Request):
    return HttpResponse("This is admission view")

def admission_report(Request):
    return HttpResponse("This is admission report view.")
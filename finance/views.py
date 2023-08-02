from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def fee_collection(request):
    return HttpResponse("This is a fee collection view")


def fee_due_report(request):
    return HttpResponse("This is a fee due report view")


def fee_collection_report(request):
    return HttpResponse("This is a fee collection report")

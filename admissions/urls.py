from django.urls import path
from admissions import views

urlpatterns = [

    path('newadm/', views.admission),
    path('admreport/', views.admission_report),
]
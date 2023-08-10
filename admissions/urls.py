from django.urls import path
from admissions import views

urlpatterns = [

    path('newadm/', views.add_admission),
    path('admreport/', views.admission_report),
]
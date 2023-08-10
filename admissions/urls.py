from django.urls import path
from admissions import views

urlpatterns = [

    path('newadm/', views.add_admission),
    path('admreport/', views.admission_report),
    path('delete/<int:id>/', views.delete_student),
    path('update/<int:id>/', views.update_student),
]
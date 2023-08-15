from django.urls import path
from admissions import views

urlpatterns = [

    path('newadm/', views.add_admission),
    path('admreport/', views.admission_report),
    path('delete/<int:id>/', views.delete_student),
    path('update/<int:id>/', views.update_student),

    path('firstclassbasedview/', views.FirstClassBasedView.as_view()),
    path('teacherslist/', views.TeacherRead.as_view(), name='teacherlisturl'),
    path('getteacherdetails/<int:pk>/', views.GetTeacher.as_view()),
    path('addteacher/', views.AddTeacher.as_view()),
    path('updateteacher/<int:pk>/', views.UpdateTeacher.as_view()),
    path('deleteteacher/<int:pk>/', views.DeleteTeacher.as_view()),
]
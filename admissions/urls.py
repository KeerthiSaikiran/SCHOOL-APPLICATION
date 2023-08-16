from django.contrib.auth.decorators import login_required
from django.urls import path
from admissions import views

urlpatterns = [

    path('newadm/', views.add_admission),
    path('admreport/', views.admission_report),
    path('delete/<int:id>/', views.delete_student),
    path('update/<int:id>/', views.update_student),

    path('firstclassbasedview/', login_required(views.FirstClassBasedView.as_view())),
    path('teacherslist/', login_required(views.TeacherRead.as_view()), name='teacherlisturl'),
    path('getteacherdetails/<int:pk>/', login_required(views.GetTeacher.as_view())),
    path('addteacher/', login_required(views.AddTeacher.as_view())),
    path('updateteacher/<int:pk>/', login_required(views.UpdateTeacher.as_view())),
    path('deleteteacher/<int:pk>/', login_required(views.DeleteTeacher.as_view())),

    path('accounts/logout/', views.userlogout),
]
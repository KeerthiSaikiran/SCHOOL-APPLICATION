from django.urls import path
from finance import views

urlpatterns = [

    path('feecoll/', views.fee_collection),
    path('feeduereport/', views.fee_due_report),
    path('feecollreport/', views.fee_collection_report),
]
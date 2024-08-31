# services/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('transportation/', views.transportation_list, name='transportation_list'),
    path('boarding/', views.boarding_list, name='boarding_list'),
    # Add more paths as needed
]

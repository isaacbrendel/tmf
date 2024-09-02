from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('members/', views.members, name='members'),
    path('services/', views.services, name='services'),
    path('feedback/', views.feedback, name='feedback'),
]

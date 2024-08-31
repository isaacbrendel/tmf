# feedback/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.feedback_list, name='feedback_list'),
    # Add more paths as needed
]

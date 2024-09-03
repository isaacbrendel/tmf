# tasks/urls.py
from django.urls import path
from .views import index
from django.contrib.auth.decorators import login_required

app_name = 'tasks'

urlpatterns = [
    path('', login_required(index), name='index'),  # Index view for listing all tasks
]

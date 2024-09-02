# tasks/urls.py
from django.urls import path
from .views import index

app_name = 'tasks'

urlpatterns = [
    path('', index, name='index'),  # Index view for listing all tasks
]

# employees/urls.py
from django.urls import path
from .views import index

app_name = 'employees'

urlpatterns = [
    path('', index, name='index'),  # Index view for listing all employees
]

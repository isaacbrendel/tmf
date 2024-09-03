# employees/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import index, employee_login_view, employee_create_view
from django.contrib.auth.decorators import login_required

app_name = 'employees'

urlpatterns = [
    path('', login_required(index), name='index'),  # Index view for listing all employees
    path('login/', employee_login_view, name='employee_login'),
    path('create/', employee_create_view, name='employee_create'),   
    path('logout/', LogoutView.as_view(next_page='employees:employee_login'), name='logout'),  # Add the logout view
]

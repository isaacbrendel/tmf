# employees/views.py
from django.shortcuts import render
from .models import Employee

def index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})

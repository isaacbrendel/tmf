# employees/views.py
from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import EmployeeCreationForm

@login_required
def index(request):
    employees = Employee.objects.all()
    return render(request, 'employees/index.html', {'employees': employees})

def employee_create_view(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_login')
    else:
        form = EmployeeCreationForm()

    return render(request, 'employees/create_employee.html', {'form': form})

def employee_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:index')
    else:
        form = AuthenticationForm()

    return render(request, 'employees/login.html', {'form': form})
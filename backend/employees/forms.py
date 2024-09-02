from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee

class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'email', 'phone_number', 'role', 'password1', 'password2']

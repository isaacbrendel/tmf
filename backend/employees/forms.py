from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Employee
from django.contrib.auth.forms import AuthenticationForm

class EmployeeLoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Username'})
    )
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
    )

class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = Employee
        fields = ['username', 'email', 'phone_number', 'role', 'password1', 'password2']

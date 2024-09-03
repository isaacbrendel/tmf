from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class MemberLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

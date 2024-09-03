from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import MemberLoginForm

def member_login_view(request):
    if request.method == 'POST':
        form = MemberLoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:index')  # Redirect to the dashboard after login
    else:
        form = MemberLoginForm()
    
    return render(request, 'members/member_login.html', {'form': form})

def member_form_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_form')
    else:
        form = CustomUserForm()
    
    return render(request, 'members/member_form.html', {'form': form})

@login_required(login_url='employees:login')
def index(request):
    members = CustomUser.objects.all()  # Fetch all members from the CustomUser model
    return render(request, 'members/index.html', {'members': members})
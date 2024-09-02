# dashboard/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='employees:login')
def index(request):
    return render(request, 'dashboard/index.html')

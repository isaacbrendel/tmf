# tasks/views.py
from django.shortcuts import render
from .models import Task
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/index.html', {'tasks': tasks})

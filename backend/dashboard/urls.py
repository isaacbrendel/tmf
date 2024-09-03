# dashboard/urls.py
from django.urls import path
from .views import index
from django.contrib.auth.decorators import login_required

app_name = 'dashboard'  # Ensure the app_name is set correctly

urlpatterns = [
    path('', login_required(index), name='index'),
]

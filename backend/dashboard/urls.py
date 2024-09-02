# dashboard/urls.py
from django.urls import path
from .views import index

app_name = 'dashboard'  # Ensure the app_name is set correctly

urlpatterns = [
    path('', index, name='index'),
]

# services/urls.py
from django.urls import path
from .views import transportation_form_view, boarding_form_view, index

app_name = 'services'  # This defines the namespace

urlpatterns = [
    path('transportation-form/', transportation_form_view, name='transportation_form_view'),
    path('boarding-form/', boarding_form_view, name='boarding_form_view'),
    path('dashboard/', index, name='index'),  # Add the index view
]

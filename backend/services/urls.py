from django.urls import path
from .views import transportation_form_view, boarding_form_view

urlpatterns = [
    path('', transportation_form_view, name='transportation_form'),
    path('boarding-form/', boarding_form_view, name='boarding_form'),
]

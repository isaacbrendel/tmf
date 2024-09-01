from django.urls import path
from .views import feedback_form_view

urlpatterns = [
    path('feedback-form/', feedback_form_view, name='feedback_form'),
]

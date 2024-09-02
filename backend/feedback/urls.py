# feedback/urls.py
from django.urls import path
from .views import index, feedback_form_view

app_name = 'feedback'

urlpatterns = [
    path('dashboard', index, name='index'),  # Index view for listing all feedback
    path('feedback-form/', feedback_form_view, name='feedback_form_view'),
]

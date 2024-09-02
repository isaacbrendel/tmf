# feedback/urls.py
from django.urls import path
from .views import feedback_form_view, index

app_name = 'feedback'

urlpatterns = [
    path('feedback-form/', feedback_form_view, name='feedback_form'),
    path('', index, name='index'),  # Index view for listing all feedback
]

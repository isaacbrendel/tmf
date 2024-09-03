from django.urls import path
from .views import services_view, members_view, feedback_view

app_name = 'home'

urlpatterns = [
    path('', services_view, name='services'),
    path('members/', members_view, name='members'),
    path('feedback/', feedback_view, name='feedback'),
]

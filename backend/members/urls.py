from django.urls import path
from .views import member_form_view

urlpatterns = [
    path('member-form/', member_form_view, name='member_form'),
]

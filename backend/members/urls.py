# members/urls.py
from django.urls import path
from .views import index, member_form_view

app_name = 'members'  # Add this line to define the namespace

urlpatterns = [
    path('dashboard/', index, name='index'),  # Add the index view
    path('member-form/', member_form_view, name='member_form_view'),
]

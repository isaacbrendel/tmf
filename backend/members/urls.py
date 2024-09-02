# members/urls.py
from django.urls import path
from .views import member_form_view, index

app_name = 'members'  # Add this line to define the namespace

urlpatterns = [
    path('member-form/', member_form_view, name='member_form'),
    path('', index, name='index'),  # Add the index view
]

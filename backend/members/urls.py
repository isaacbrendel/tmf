# members/urls.py
from django.urls import path
from .views import index, member_form_view, member_login_view
from django.contrib.auth.decorators import login_required

app_name = 'members'  # Add this line to define the namespace

urlpatterns = [
    path('', login_required(index), name='index'),  # Add the index view
    path('member-form/', member_form_view, name='member_form_view'),
    path('member-login/', member_login_view, name='member_login_view'),
]

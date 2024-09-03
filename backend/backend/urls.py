"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),  # Public-facing home page
    path('grappelli/', include('grappelli.urls')),  # Grappelli admin interface

    # Dashboard Section - Everything here is under dashboard
    path('dashboard/', include([
        path('', include('dashboard.urls')),  # Dashboard root
        path('members/', include('members.urls')),  # Dashboard members
        path('services/', include('services.urls')),  # Dashboard services
        path('feedback/', include('feedback.urls')),  # Dashboard feedback
        path('tasks/', include('tasks.urls')),  # Dashboard tasks
        path('assets/', include('assets.urls')),  # Dashboard assets
        path('employees/', include('employees.urls')),  # Dashboard employees
    ])),
]

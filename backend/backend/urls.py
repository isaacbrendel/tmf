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
    path("members/", include("members.urls")),
    path("", include("home.urls")),
    path("feedback/", include("feedback.urls")),
    path('grappelli/', include('grappelli.urls')),  # Grappelli admin interface
    path('dashboard/', include('dashboard.urls')),  # Dashboard
    path("tasks/", include("tasks.urls")),
    path("assets/", include("assets.urls")),
    path("employees/", include("employees.urls")),
    
    # Dashboard Section
    path('dashboard/services/', include('services.urls')),
    path('dashboard/feedback/', include('feedback.urls')),
    path('dashboard/tasks/', include('tasks.urls')),
    path('dashboard/assets/', include('assets.urls')),
    path('dashboard/employees/', include('employees.urls')),
    path('dashboard/', include('dashboard.urls')),  # Dashboard root
]

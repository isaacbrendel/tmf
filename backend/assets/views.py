# assets/views.py
from django.shortcuts import render
from .models import Asset
from django.contrib.auth.decorators import login_required # Import the login_required decorator

@login_required  # Apply the login_required decorator to the index view
def index(request):
    assets = Asset.objects.all()
    return render(request, 'assets/index.html', {'assets': assets})

from django.shortcuts import render, redirect
from .forms import CustomUserForm
from .models import CustomUser

def member_form_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('member_form')
    else:
        form = CustomUserForm()
    
    return render(request, 'members/member_form.html', {'form': form})


def index(request):
    members = CustomUser.objects.all()  # Fetch all members from the CustomUser model
    return render(request, 'members/index.html', {'members': members})
from django.shortcuts import render, redirect
from .forms import HorseTransportationForm, HorseBoardingForm

def transportation_form_view(request):
    if request.method == 'POST':
        form = HorseTransportationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transportation_form')
    else:
        form = HorseTransportationForm()
    
    return render(request, 'services/transportation_form.html', {'form': form})

def boarding_form_view(request):
    if request.method == 'POST':
        form = HorseBoardingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boarding_form')
    else:
        form = HorseBoardingForm()
    
    return render(request, 'services/boarding_form.html', {'form': form})

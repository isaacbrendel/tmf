from django.shortcuts import render, redirect
from .forms import HorseTransportationForm, HorseBoardingForm
from .models import HorseTransportation, HorseBoarding  # Import the models
from tasks.models import Task
from django.contrib.auth.decorators import login_required




def transportation_form_view(request):
    if request.method == 'POST':
        form = HorseTransportationForm(request.POST)
        if form.is_valid():
            transportation = form.save()

            # Create a task for this transportation service
            Task.objects.create(
                title=f"Transport {transportation.number_of_horses} horses",
                description=transportation.description or f"Transportation request on {transportation.date}",
                status=Task.TO_DO,  # Set status using predefined choice
                due_date=transportation.date,  # You can adjust the due date logic as needed
                service_request=None  # Placeholder if service request model is not defined yet
            )
            return redirect('transportation_form')
    else:
        form = HorseTransportationForm()

    return render(request, 'services/transportation_form.html', {'form': form})

def boarding_form_view(request):
    if request.method == 'POST':
        form = HorseBoardingForm(request.POST)
        if form.is_valid():
            boarding = form.save()

            # Create a task for this boarding service
            Task.objects.create(
                title=f"Board {boarding.number_of_animals} animals",
                description=boarding.description or f"Boarding request from {boarding.start_date} to {boarding.end_date}",
                status=Task.TO_DO,  # Set status using predefined choice
                due_date=boarding.end_date or boarding.start_date,  # Use start_date if no end_date
                service_request=None  # Placeholder if service request model is not defined yet
            )
            return redirect('boarding_form')
    else:
        form = HorseBoardingForm()

    return render(request, 'services/boarding_form.html', {'form': form})

@login_required
def index(request):
    transportations = HorseTransportation.objects.all()  # Get all HorseTransportation objects
    boardings = HorseBoarding.objects.all()  # Get all HorseBoarding objects
    
    context = {
        'transportations': transportations,
        'boardings': boardings,
    }
    return render(request, 'services/index.html', context)

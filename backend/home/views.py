# home/views.py
from django.shortcuts import render
from members.forms import CustomUserForm
from services.forms import HorseTransportationForm, HorseBoardingForm
from feedback.forms import FeedbackForm

def home(request):
    member_form = CustomUserForm()
    services_form = HorseTransportationForm()  # Adjust if you're showing both forms
    feedback_form = FeedbackForm()

    context = {
        'member_form': member_form,
        'services_form': services_form,
        'feedback_form': feedback_form,
    }
    
    return render(request, 'home/index.html', context)

def members(request):
    form = CustomUserForm()
    return render(request, 'home/members.html', {'form': form})

def services(request):
    transportation_form = HorseTransportationForm()
    boarding_form = HorseBoardingForm()
    return render(request, 'home/services.html', {
        'transportation_form': transportation_form,
        'boarding_form': boarding_form
    })

def feedback(request):
    form = FeedbackForm()
    return render(request, 'home/feedback.html', {'form': form})

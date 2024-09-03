from django.shortcuts import render, redirect
from services.forms import HorseTransportationForm, HorseBoardingForm
from members.forms import CustomUserForm
from feedback.forms import FeedbackForm

def services_view(request):
    if request.method == 'POST':
        transport_form = HorseTransportationForm(request.POST, prefix='transport')
        boarding_form = HorseBoardingForm(request.POST, prefix='boarding')
        
        if transport_form.is_valid():
            transport_form.save()
            return redirect('home:services')
        elif boarding_form.is_valid():
            boarding_form.save()
            return redirect('home:services')
    else:
        transport_form = HorseTransportationForm(prefix='transport')
        boarding_form = HorseBoardingForm(prefix='boarding')

    return render(request, 'home/services.html', {
        'transport_form': transport_form,
        'boarding_form': boarding_form
    })


def members_view(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:members')
    else:
        form = CustomUserForm()

    return render(request, 'home/members.html', {'form': form})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home:feedback')
    else:
        form = FeedbackForm()

    return render(request, 'home/feedback.html', {'form': form})

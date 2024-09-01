from django import forms
from .models import HorseTransportation, HorseBoarding

class HorseTransportationForm(forms.ModelForm):
    class Meta:
        model = HorseTransportation
        fields = ['number_of_horses', 'date', 'distance']

class HorseBoardingForm(forms.ModelForm):
    class Meta:
        model = HorseBoarding
        fields = ['number_of_animals', 'start_date', 'end_date']

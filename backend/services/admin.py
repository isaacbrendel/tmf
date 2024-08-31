# services/admin.py

from django.contrib import admin
from .models import HorseTransportation, HorseBoarding

admin.site.register(HorseTransportation)
admin.site.register(HorseBoarding)

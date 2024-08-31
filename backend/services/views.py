# services/views.py

from django.http import HttpResponse

def transportation_list(request):
    return HttpResponse("List of Horse Transportation services.")

def boarding_list(request):
    return HttpResponse("List of Horse Boarding services.")

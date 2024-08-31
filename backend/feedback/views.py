# feedback/views.py

from django.http import HttpResponse

def feedback_list(request):
    return HttpResponse("List of Feedback.")

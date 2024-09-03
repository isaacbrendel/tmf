# feedback/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.contrib.auth.decorators import login_required

def feedback_form_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feedback:feedback_form_view')  # Redirect back to the form after submission
    else:
        form = FeedbackForm()

    return render(request, 'feedback/feedback_form.html', {'form': form})

@login_required(login_url='employees:login')
def index(request):
    feedback_list = Feedback.objects.all()
    return render(request, 'feedback/index.html', {'feedback_list': feedback_list})

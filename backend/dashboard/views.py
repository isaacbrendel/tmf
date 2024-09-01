from django.shortcuts import render, redirect
import plotly.graph_objects as go
from django.utils.safestring import mark_safe
from services.models import HorseTransportation, HorseBoarding
from feedback.models import Feedback
from services.forms import HorseTransportationForm, HorseBoardingForm
from feedback.forms import FeedbackForm
import pandas as pd
from django.db.models import Count  # Import Count

def dashboard_view(request):
    # Handle form submissions
    if request.method == 'POST':
        if 'transport_form' in request.POST:
            transport_form = HorseTransportationForm(request.POST)
            if transport_form.is_valid():
                transport_form.save()
                return redirect('dashboard')

        if 'boarding_form' in request.POST:
            boarding_form = HorseBoardingForm(request.POST)
            if boarding_form.is_valid():
                boarding_form.save()
                return redirect('dashboard')

        if 'feedback_form' in request.POST:
            feedback_form = FeedbackForm(request.POST, request.FILES)
            if feedback_form.is_valid():
                feedback_form.save()
                return redirect('dashboard')
    else:
        transport_form = HorseTransportationForm()
        boarding_form = HorseBoardingForm()
        feedback_form = FeedbackForm()

    # Horse Transportation Scatter Plot
    transportation_data = HorseTransportation.objects.all()
    if transportation_data.exists():
        df_transport = pd.DataFrame(list(transportation_data.values('date', 'distance')))
        df_transport['date'] = pd.to_datetime(df_transport['date'])
        df_transport.sort_values('date', inplace=True)
        
        transport_scatter = go.Figure()
        transport_scatter.add_trace(go.Scatter(
            x=df_transport['date'],
            y=df_transport['distance'],
            mode='markers',
            marker=dict(size=10, color='#FF5733'),
            text=df_transport['distance'],
            name='Distance (miles)'
        ))
        transport_scatter.update_layout(
            title='Horse Transportation Data Points',
            xaxis_title='Date',
            yaxis_title='Distance (miles)',
            showlegend=False,
            template='simple_white'
        )
        transport_scatter = transport_scatter.to_html(full_html=False)
    else:
        transport_scatter = "<p>No transportation data available.</p>"

    # Horse Boarding Scatter Plot
    boarding_data = HorseBoarding.objects.all()
    if boarding_data.exists():
        df_boarding = pd.DataFrame(list(boarding_data.values('start_date', 'number_of_animals')))
        df_boarding['start_date'] = pd.to_datetime(df_boarding['start_date'])
        df_boarding.sort_values('start_date', inplace=True)

        boarding_scatter = go.Figure()
        boarding_scatter.add_trace(go.Scatter(
            x=df_boarding['start_date'],
            y=df_boarding['number_of_animals'],
            mode='markers',
            marker=dict(size=10, color='#33FF57'),
            text=df_boarding['number_of_animals'],
            name='Number of Animals'
        ))
        boarding_scatter.update_layout(
            title='Horse Boarding Data Points',
            xaxis_title='Start Date',
            yaxis_title='Number of Animals',
            showlegend=False,
            template='simple_white'
        )
        boarding_scatter = boarding_scatter.to_html(full_html=False)
    else:
        boarding_scatter = "<p>No boarding data available.</p>"

    # Feedback Scatter Plot
    feedback_data = Feedback.objects.values('stars').annotate(total=Count('id'))
    if feedback_data.exists():
        df_feedback = pd.DataFrame(list(feedback_data))

        feedback_scatter = go.Figure()
        feedback_scatter.add_trace(go.Scatter(
            x=df_feedback.index,
            y=df_feedback['stars'],
            mode='markers',
            marker=dict(size=10, color='#3357FF'),
            text=df_feedback['total'],
            name='Stars'
        ))
        feedback_scatter.update_layout(
            title='Feedback Data Points',
            xaxis_title='Feedback ID',
            yaxis_title='Stars',
            showlegend=False,
            template='simple_white'
        )
        feedback_scatter = feedback_scatter.to_html(full_html=False)
    else:
        feedback_scatter = "<p>No feedback data available.</p>"

    context = {
        'transport_scatter': mark_safe(transport_scatter),
        'boarding_scatter': mark_safe(boarding_scatter),
        'feedback_scatter': mark_safe(feedback_scatter),
        'transport_form': transport_form,
        'boarding_form': boarding_form,
        'feedback_form': feedback_form,
    }
    return render(request, 'dashboard/dashboard.html', context)

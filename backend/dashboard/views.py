from django.shortcuts import render
import plotly.express as px
from django.utils.safestring import mark_safe
from services.models import HorseTransportation, HorseBoarding
from feedback.models import Feedback
from django.db.models import Avg, Count
from datetime import date

def dashboard_view(request):
    # Horse Transportation Data Visualization
    transportation_data = HorseTransportation.objects.all()
    if transportation_data.exists():
        df_transport = pd.DataFrame(list(transportation_data.values('date', 'number_of_horses', 'distance')))
        transport_fig = px.line(df_transport, x='date', y='distance',
                                title='Horse Transportation Distance Over Time')
        transport_graph = transport_fig.to_html(full_html=False)
    else:
        transport_graph = "<p>No transportation data available.</p>"

    # Horse Boarding Data Visualization
    boarding_data = HorseBoarding.objects.all()
    if boarding_data.exists():
        df_boarding = pd.DataFrame(list(boarding_data.values('start_date', 'number_of_animals')))
        boarding_fig = px.bar(df_boarding, x='start_date', y='number_of_animals',
                              title='Horse Boarding - Number of Animals Over Time')
        boarding_graph = boarding_fig.to_html(full_html=False)
    else:
        boarding_graph = "<p>No boarding data available.</p>"

    # Feedback Data Visualization
    feedback_data = Feedback.objects.values('category').annotate(total=Count('id'))
    if feedback_data.exists():
        df_feedback = pd.DataFrame(list(feedback_data))
        feedback_fig = px.pie(df_feedback, values='total', names='category',
                              title='Feedback Distribution')
        feedback_graph = feedback_fig.to_html(full_html=False)
    else:
        feedback_graph = "<p>No feedback data available.</p>"

    context = {
        'transport_graph': mark_safe(transport_graph),
        'boarding_graph': mark_safe(boarding_graph),
        'feedback_graph': mark_safe(feedback_graph),
    }
    return render(request, 'dashboard/dashboard.html', context)

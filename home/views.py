from django.shortcuts import render
from events.models import Event
from datetime import datetime


def index(request):
    """ homepage view """
    current_date = datetime.now()
    upcoming_events = Event.objects.filter(
        date__gte=current_date).order_by('date')[:3]
    return render(request, 'home/index.html', {'upcoming_events': upcoming_events})

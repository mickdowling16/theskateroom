from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Event
from .forms import RegistrationForm
from django.urls import reverse


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    return render(request, 'events/event_detail.html', {'event': event})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process the form data (e.g., save it to the database)

            # Add a success message
            messages.success(
                request, 'Thank you for registering your interest.')

            # Redirect to a thank-you page or do something else
            # Make sure you have a 'thank_you_page' URL name
            return redirect('thank_you_page')

    else:
        form = RegistrationForm()

    return render(request, 'events/register.html', {'form': form})

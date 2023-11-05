from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Event
from .forms import RegistrationForm
from comments.models import Comment
from django.urls import reverse


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)

    comments = Comment.objects.filter(event=event)

    context = {
        'event': event,
        'comments': comments,
    }

    return render(request, 'events/event_detail.html', context)


def register(request):

    if request.method == 'POST':
        messages.success(
            request, f'Thank you for registering for event')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return redirect('events:event_list')

    else:
        # Set the queryset for the event field to display events in the dropdown
        form = RegistrationForm()
        form.fields['event'].queryset = Event.objects.all()

    return render(request, 'events/register.html', {'form': form})

from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Event
from .forms import RegistrationForm, EventForm
from comments.models import Comment
from comments.forms import CommentForm
from django.urls import reverse


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    event = Event.objects.get(pk=event_id)
    comments = Comment.objects.filter(event=event).order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'events/event_detail.html', {'event': event, 'comments': comments, 'comment_form': comment_form})


def register(request):

    if request.method == 'POST':
        messages.success(
            request, f'Thank you for registering for event')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            return redirect('events:event_list')

    else:
        form = RegistrationForm()
        form.fields['event'].queryset = Event.objects.all()

    return render(request, 'events/register.html', {'form': form})


def add_event(request):
    """ Add an event to the website """
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added an event!')
            return redirect(reverse('events:add_event'))
        else:
            messages.error(
                request, 'Failed to add a new event. Please ensure the form is valid.')
    else:
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_event(request, event_id):
    """ Edit an event on the website """
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated event!')
            return redirect(reverse('events:event_detail', args=[event.id]))
        else:
            messages.error(
                request, 'Failed to update event. Please ensure the form is valid.')
    else:
        form = EventForm(instance=event)
        messages.info(request, f'You are editing {event.title}')

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': event,
    }

    return render(request, template, context)

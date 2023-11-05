from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Event
from .forms import RegistrationForm
from comments.models import Comment
from comments.forms import CommentForm
from django.urls import reverse


def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    # Your existing code
    event = Event.objects.get(pk=event_id)
    comments = Comment.objects.filter(event=event)
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
        # Set the queryset for the event field to display events in the dropdown
        form = RegistrationForm()
        form.fields['event'].queryset = Event.objects.all()

    return render(request, 'events/register.html', {'form': form})

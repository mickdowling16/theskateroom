from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from .models import Event, Registration
from .forms import RegistrationForm, EventForm
from comments.models import Comment
from comments.forms import CommentForm
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings


def event_list(request):
    """ list of all events on website """
    events = Event.objects.all().order_by('date')
    return render(request, 'events/event_list.html', {'events': events})


def event_detail(request, event_id):
    """ More detail on each event """
    event = Event.objects.get(pk=event_id)
    comments = Comment.objects.filter(event=event).order_by('-created_at')
    comment_form = CommentForm()
    return render(request, 'events/event_detail.html', {'event': event, 'comments': comments, 'comment_form': comment_form})


def register(request):
    """ Register interest in event from Registration Form """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            event = form.cleaned_data['event']
            message = form.cleaned_data['message']

            registration = Registration(
                name=name,
                email=email,
                phone=phone,
                event=event,
                message=message
            )
            registration.save()

            # Send email with form details
            subject = f'New Registration for {event}'
            message = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nEvent: {event}\nMessage: {message}"

            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, ['theskateroom2023@gmail.com'])

            # Redirect or render a success page
            messages.success(request, f"Thank you for registering for {event}.")
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
            event = form.save()
            messages.success(request, 'Successfully added new event')
            return redirect(reverse('events:event_detail', args=[event.id]))
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


def delete_event(request, event_id):
    """ Delete an event from the website """
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events:event_list'))

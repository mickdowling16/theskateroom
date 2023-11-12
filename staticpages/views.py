from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    """ Add view for contact form submissions """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            subject = 'Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = 'info@theskateroom.com'
            recipient_list = ['theskateroom2023@gmail.com']

            # Send the email
            send_mail(subject, message, from_email, recipient_list)

            # Add a success message
            messages.success(request, 'Your message was sent successfully!')

            # Redirect to the home page after successful submission
            return redirect('home')

    else:
        form = ContactForm()

    return render(request, 'staticpages/contact.html', {'form': form})

def skateparks(request):
    """ View to render local skateparks page """
    return render(request, 'staticpages/skateparks.html')

def policy(request):
    """ View to render privacy policy page """
    return render(request, 'staticpages/policy.html')
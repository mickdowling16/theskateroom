from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            subject = 'Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = 'theskateroom@example.com'
            recipient_list = ['theskateroom2023@gmail.com'] 

            # Send the email
            send_mail(subject, message, from_email, recipient_list)

            # Display success message when form submitted
            messages.success(request, 'Contact form submitted.')

    else:
        form = ContactForm()

    return render(request, 'staticpages/contact.html', {'form': form})

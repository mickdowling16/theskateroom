from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the form data
            subject = 'Contact Form Submission'
            message = f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nMessage: {form.cleaned_data['message']}"
            from_email = 'your_email@example.com'  # Update with your email
            recipient_list = ['theskateroom2023@gmail.com']  # Update with recipient email(s)

            # Send the email
            send_mail(subject, message, from_email, recipient_list)

            # Add a success message
            messages.success(request, 'Your message was sent successfully!')

            # Redirect to the home page after successful submission
            return redirect('home')  # Update with the actual name or URL of your home page

    else:
        form = ContactForm()

    return render(request, 'staticpages/contact.html', {'form': form})

def skateparks(request):
    return render(request, 'staticpages/skateparks.html')
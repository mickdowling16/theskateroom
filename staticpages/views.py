from django.shortcuts import render
from .forms import ContactForm 


def contact(request):
    return render(request, 'staticpages/contact.html', {})

from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    form = ContactForm()
    return render(request, '/workspaces/theskateroom/staticpages/templates/staticpages/contact.html', {'form': form})

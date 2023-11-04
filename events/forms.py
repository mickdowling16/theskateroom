from django import forms
from .models import Event


class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)
    event = forms.ModelChoiceField(
        queryset=Event.objects.all(),
        empty_label='Select an event',
    )
    message = forms.CharField(max_length=500)

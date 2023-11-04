from django import forms
from .models import Event


class RegistrationForm(forms.Form):
    event = forms.ModelChoiceField(queryset=Event.objects.all())
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

from django.forms import SelectDateWidget
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


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['time'].widget = forms.TimeInput(attrs={'type': 'time'})


        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

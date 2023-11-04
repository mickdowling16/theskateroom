from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['has_sizes']
        fields = ['size']  # Include any other fields you need

    # Define the size field as a ChoiceField with predefined options
    size = forms.ChoiceField(
        choices=[('Small', 'Small'), ('Medium', 'Medium'),
                 ('Large', 'Large'), ('Extra Large', 'Extra Large')],
        widget=forms.Select(
            attrs={'class': 'form-control', 'style': 'height: 50px;'}),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

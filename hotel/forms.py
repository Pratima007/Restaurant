# forms.py
from django import forms
from .models import Second


class SecondForm(forms.ModelForm):
    class Meta:
        model = Second
        fields = ['name', 'price', 'image']

    def clean_price(self):
        price = self.cleaned_data.get('price')
        try:
            price = round(float(price), 2)
        except (ValueError, TypeError):
            raise forms.ValidationError("Enter a valid decimal value for the price.")
        return price


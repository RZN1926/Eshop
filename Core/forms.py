from django import forms
from .models import Product

class DatePicker(forms.DateInput):
    input_type = 'date'

class ProductForm(forms.ModelForm):
    guarantee = forms.DateField(
        widget = DatePicker,
        label = 'Guarantee',
        required = False
    )
    expiration_date = forms.DateField(
        widget = DatePicker,
        label = 'Use before',
        required = False
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'qty',
            'category',
            'guarantee',
            'expiration_date'
        ]


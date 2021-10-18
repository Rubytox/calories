from django import forms
from django.core import validators

class AddFoodManualForm(forms.Form):
    name = forms.CharField(label='Product name', max_length=200)
    barcode = forms.CharField(label='Barcode of the product', max_length=100)
    quantity = forms.FloatField(label='Eaten quantity (g)', min_value=0)

class AddFoodFormManual(forms.Form):
    name = forms.CharField(label='Product name', max_length=200)

    energy = forms.IntegerField(label='Energy', min_value=0)
    fat = forms.FloatField(label='Fat', min_value=0)
    saturated_fat = forms.FloatField(label='Saturated fat', min_value=0)
    carbohydrates = forms.FloatField(label='Carbohydrates', min_value=0)
    sugars = forms.FloatField(label='Sugars', min_value=0)
    fibers = forms.FloatField(label='Fibers', min_value=0)
    proteins = forms.FloatField(label='Proteins', min_value=0)
    salt = forms.FloatField(label='Salt', min_value=0)

    quantity = forms.FloatField(label='Eaten quantity (g)', min_value=0)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""
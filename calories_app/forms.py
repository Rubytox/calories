from django import forms

class AddFoodForm(forms.Form):
    name = forms.CharField(label='Product name', max_length=200)
    barcode = forms.CharField(label='Barcode of the product', max_length=100)
    quantity = forms.FloatField(label='Eaten quantity (g)')

class AddFoodFormManual(forms.Form):
    name = forms.CharField(label='Product name', max_length=200)

    energy = forms.IntegerField(label='Energy (kcal)')
    fat = forms.FloatField(label='Fat (g)')
    saturated_fat = forms.FloatField(label='Saturated fat (g)')
    carbohydrates = forms.FloatField(label='Carbohydrates (g)')
    sugars = forms.FloatField(label='Sugars (g)')
    fibers = forms.FloatField(label='Fibers (g)')
    proteins = forms.FloatField(label='Proteins (g)')
    salt = forms.FloatField(label='Salt (g)')

    quantity = forms.FloatField(label='Eaten quantity (g)')
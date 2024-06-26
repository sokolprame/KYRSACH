from django import forms

class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(label='Количество', min_value=1)

from django import forms

class PurchaseForm(forms.Form):
    quantity = forms.IntegerField(label='����������', min_value=1)

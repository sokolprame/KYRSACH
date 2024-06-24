from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from goods.models import Order

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['address', 'card_number', 'expiration_date', 'cvv']

from django import forms
from .models import Product, ProductVariant

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'brand', 'is_new', 'is_popular', 'is_discounted']

class ProductVariantForm(forms.ModelForm):
    class Meta:
        model = ProductVariant
        fields = ['product', 'size', 'color', 'stock']
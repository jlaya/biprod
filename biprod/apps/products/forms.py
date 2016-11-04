#encoding:utf-8
from django.forms import ModelForm
from django import forms
from biprod.apps.products.models import Products

class ProductsForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['nombre', 'descripcion', 'stock', 'precio','foto']

from django.core import validators
from django import forms
from .models import Product,Ownshop
from django.forms import ModelForm

class AddProduct(ModelForm):
    class Meta:
        model=Product
        fields=['product','price','product_details','product_image']
        labels={
            'product':'product name',
            'price':'product price'
        }
        widgets={
            'product':forms.TextInput(attrs={
            'class':"procuctclass",
            'placeholder':'items name',

            }),
            'price':forms.NumberInput(attrs={
            'class':"procuctclass",
            'placeholder':'items price',

            }),
            'product_details':forms.Textarea(attrs={
            'class':"procuctclass ptrs",
            'id':"procuctdetailsid",
            'placeholder':'items details',

            }),
            'product_image':forms.ClearableFileInput(attrs={
            'class':"procuctclass",
            'class':"procuctimagid",
            'placeholder':'items name',

            }),
        }
       

class AddShop(ModelForm):
    class Meta:
        model=Ownshop
        fields=['shop_name','shop_ownername','ph_no','address']
        widgets={
            'shop_name':forms.TextInput(attrs={
            'class':"procuctclass",
            'placeholder':'items name',

            }),
            'shop_ownername':forms.TextInput(attrs={
            'class':"procuctclass",
            'placeholder':'owner name',

            }),
            'ph_no':forms.NumberInput(attrs={
            'class':"procuctclass",
            'placeholder':'items price',

            }),
            'address':forms.Textarea(attrs={
            'class':"procuctclass ptrs",
            'id':"procuctdetailsid",
            'placeholder':'items details',

            }),
        }
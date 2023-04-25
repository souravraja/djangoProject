from django import forms

class Search(forms.Form):
    name=forms.CharField(label="",required=False,widget=forms.TextInput(attrs={'placeholder':'type to search',}))
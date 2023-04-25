
# import form class from django

from django import forms
from .models import Post
from django.forms import ModelForm
          
class PostForm(ModelForm): 
  class Meta:
    model = Post
    fields = ['title','description','image']
    labels={'title':'your title'}
    widgets={
      'title':forms.TextInput(attrs={'class':'yourclass','placeholder': 'POST TITLE HEAR....'}),
      'description':forms.Textarea(attrs={'class':'yourdescription','placeholder': 'write something.............'}),
      
    }
    
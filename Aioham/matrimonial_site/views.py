from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import matrimonial,image
# Create your views here.

class MatrimonialHome(ListView):
    model=matrimonial
    template_name='matrimonial_site/home1.html'
    context_object_name='context'
    



class CreateMatrimonialPost(LoginRequiredMixin,CreateView):
    model=matrimonial
    fields=['name','dob','gender','hobbie','profession','religion','qualification',]
    template_name='matrimonial_site/addMember.html'
    success_url='/'
    def form_valid(self, form): 
        form.instance.user=self.request.user
        return super().form_valid(form)
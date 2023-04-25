from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def online_transport(request):
    return render(request,'online_transport_booking/home.html')



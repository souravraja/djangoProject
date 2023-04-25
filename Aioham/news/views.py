from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def news(request):
    
    return render(request,'news/home.html',)

def FullNews(request,pk):
    return render(request,"news/full_news.html")
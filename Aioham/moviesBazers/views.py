from django.shortcuts import render
from django.http import HttpResponse
from moviesBazers.models import Movie,MainMovie,ScrollMovie,Showmovie

# Create your views here.

def moviehome(request):
    movie=Movie.objects.all()
    mmovie=MainMovie.objects.all()
    smovie=ScrollMovie.objects.all()
    return render(request,'moviebazer/home.html',{'m':movie,'mm':mmovie,'sm':smovie})


def ShowMovie(request,pk):
    sm=Showmovie.objects.all()
    return render(request,"moviebazer/play.html",{'sm':sm})
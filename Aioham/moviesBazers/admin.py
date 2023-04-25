from django.contrib import admin
from .models import Movie,MainMovie,ScrollMovie,Showmovie
# Register your models here.
@admin.register(Movie,MainMovie,ScrollMovie,Showmovie)
class MovieAdmin(admin.ModelAdmin):
    list_display=('id','title')
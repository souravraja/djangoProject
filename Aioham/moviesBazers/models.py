from django.db import models

# Create your models here.
class MainMovie(models.Model):
    img=models.ImageField(upload_to="mainmovieposter/")
    title=models.CharField(max_length=100)
    date=models.DateField()

    
class ScrollMovie(models.Model):
    img=models.ImageField(upload_to="scrollmovieposter/")
    title=models.CharField(max_length=100)
    date=models.DateField()

class Movie(models.Model):
    img=models.ImageField(upload_to="movieposter/")
    title=models.CharField(max_length=100)
    date=models.DateField()

class Showmovie(models.Model):
    title=models.CharField(max_length=100)
    des=models.TextField()
    img=models.ImageField(upload_to="show_movie_poster")
    video=models.FileField(upload_to='movie/')
    
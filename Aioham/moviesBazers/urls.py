
from django.urls import path
from moviesBazers import views

urlpatterns = [
    path('', views.moviehome,name='homemovie'),
    path('showmovie/<str:pk>/', views.ShowMovie,name='showmovie'),
]

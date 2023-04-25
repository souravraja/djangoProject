from django.urls import path
from news import views

urlpatterns = [
   
      path("news/",views.news,name='news1'),
      path("news/<int:pk>/",views.FullNews,name='news2'),
]
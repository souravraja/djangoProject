
from django.urls import path
from matrimonial_site import views

urlpatterns = [
   
    path("matrimonial/",views.MatrimonialHome.as_view(),name='matrimonial1'),
    path("CreateMatrimonialPost/",views.CreateMatrimonialPost.as_view(),name='CreateMatrimonialPost1')
]
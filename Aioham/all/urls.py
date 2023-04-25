from django.urls import path
from all import views

urlpatterns=[
    path("",views.all,name="allin")
]
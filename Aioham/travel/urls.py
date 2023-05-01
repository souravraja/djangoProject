from django.urls import path
from travel import views
urlpatterns=[
    path("travel/",views.index,name="travelin")
]
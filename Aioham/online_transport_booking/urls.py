from django.urls import path
from online_transport_booking import views

urlpatterns = [
   
      path("online_transport/",views.online_transport,name='online_transport1')
]
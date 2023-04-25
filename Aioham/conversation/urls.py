from django.urls import path
from conversation import views

urlpatterns = [
    path('', views.conversation,name='conversation'),
    ]
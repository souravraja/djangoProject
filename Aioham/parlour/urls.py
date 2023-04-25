from django.urls import path
from parlour import views
urlpatterns=[
  path("parlour/",views.parlour.as_view(),name="parlourhome"),
  path("createparlour/",views.CreateParlourPost.as_view(),name="parlourin"),
]
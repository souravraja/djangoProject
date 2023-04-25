from django.urls import path
from Book import views
urlpatterns=[
  path("home/",views.home,name="homein"),
  path("arrivals/",views.arrivals,name="arrivalsin"),
  path("book/<int:pk>/",views.book.as_view(),name="bookin"),
  path("book12/",views.book12.as_view(),name="bookin1"),
  path("book2/<int:pk>/",views.book1.as_view(),name="bookin2"),
  path("blog/",views.blog,name="blogin"),
  path("category/",views.category.as_view(),name="categoryin"),
  path("reviews/",views.reviews,name="reviewsin"),
  


]
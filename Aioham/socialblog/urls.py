from django.urls import path
from socialblog import views

urlpatterns=[
    path("",views.home.as_view(),name="socialblog"),
    path('CreatePost/',views.CreatePost.as_view(),name='CreatePost'),    
    # path('CreatePost/',views.CreatePost,name='CreatePost'),    
    path("<int:pk>/",views.PostDetails.as_view(),name='PostDetails'),
    path("ShortVideo/",views.ShortVideo,name='ShortVideo'),
    path("delete/<int:pk>/",views.DelateView.as_view(),name='delate'),
    path("update/<int:pk>/",views.Update.as_view(),name='update'),

]
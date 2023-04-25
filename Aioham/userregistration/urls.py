
from django.urls import path
from userregistration import views

urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
    path('home/',views.HomePage,name='home'),
    path('logout/',views.LogoutPage,name='logout'),
    path('profile/',views.profileview.as_view(),name='profile'),
    path('profile_edit/',views.Edit_profile.as_view(),name='profile_edit'),
    path('profile1/<int:pk>',views.profileview1.as_view(),name='profile1'),
]

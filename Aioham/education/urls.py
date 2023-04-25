from django.urls import path
from . import views

urlpatterns = [
    
    path('home/',views.catagory.as_view(),name='educationHome'),
    path('courses/',views.courses,name='educationCourses'),
    path('coursesfilter/<slug:data>',views.courses,name='educationCoursesfilter'),
    path('contect/',views.contect,name='educationContect'),
    # path('contect/',views.contect.as_view(),name='educationContect'),
    path('about/',views.about.as_view(),name='educationAbout'),
    
]
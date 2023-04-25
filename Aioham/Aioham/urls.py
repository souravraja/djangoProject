"""Aioham URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg/',include('userregistration.urls')),
    path('moviebazar/',include('moviesBazers.urls'),),
    path('',include('all.urls')),
    path('book',include('Book.urls')),
    path('matrimonial/',include('matrimonial_site.urls')),
    path('news',include('news.urls')),
    path('transport/',include('online_transport_booking.urls')),
    path('ownshop/',include('ownshop.urls')),
    path('parlour/',include('parlour.urls')),
    path('conversation/',include('conversation.urls')),
    path('socialblog/',include('socialblog.urls')),
    path('education/',include('education.urls')),
]
urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
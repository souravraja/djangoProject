from django.urls import path
from  ownshop import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
   path("typeofshop/",views.typeofshop,name="typeofshop"),
   path("ownshop/<int:pk>/",views.ownshop.as_view(),name="ownshopin"),
   path("ownshop/<int:pk>/<slug:data>/",views.ownshop.as_view(),name="ownshopin"),
   # path("ownshop/",views.ownshop,name="ownshopin1"),
   path("manu/<int:pk>/<slug:data>/",views.manu.as_view(),name="manu"),
   # path("manu/",views.manu.as_view(),name="manu"),
   path("nameofshop/<int:pk>/",views.nameofshop.as_view(),name="nameofshop"),
   # path("AddProduct/",views.AddProduct.as_view(),name="AddProduct"),
   path("addmanuitems/<int:pk>/",views.addmanyitems.as_view(),name="addmanuitems"),
   path("addshop/<int:pk>/",views.addshop.as_view(),name="addshop"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
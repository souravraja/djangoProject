from django.urls import path
from Doctor_Appointment import views

urlpatterns=[
    path("doctor/",views.doctor,name="DoctorAppointment")
]
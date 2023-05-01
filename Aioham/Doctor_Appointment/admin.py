from django.contrib import admin
from .models import Dieases,Doctor,Doctor_Address,Appointment

# Register your models here.
@admin.register(Dieases)
class DieasesModelAdmin(admin.ModelAdmin):
    list_display=['name','description']

@admin.register(Doctor)
class DoctorModelAdmin(admin.ModelAdmin):
    list_display=['doctor_name','doctor_image','experience','license','license_image','specalist']
                  
@admin.register(Doctor_Address)
class Doctor_AddressModelAdmin(admin.ModelAdmin):
    list_display=['doctor','chamber','pinnumber','opinngtime','closingtime']

@admin.register(Appointment)
class AppointmentModelAdmin(admin.ModelAdmin):
    list_display=['patient_name','patient_age','bloodgroup','appointment_date','doctor_name']
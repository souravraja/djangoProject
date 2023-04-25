from django.contrib import admin
from .models import Parlour_Facilitie, Employee,Parlour,User1

# Register your models here.
@admin.register(Parlour_Facilitie)
class ModelAdmin(admin.ModelAdmin):
    list_display=["name"]

@admin.register(Parlour)
class ModelAdmin(admin.ModelAdmin):
    list_display=["Name","Ph_no","Oping_Time"]


@admin.register(Employee)
class ModelAdmin(admin.ModelAdmin):
    list_display=["name","img","experience"]

@admin.register(User1)
class ModelAdmin(admin.ModelAdmin):
    list_display=["name","age","time"]

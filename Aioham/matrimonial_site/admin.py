from django.contrib import admin
from .models import matrimonial,image
# Register your models here.
@admin.register(matrimonial)
class MovieAdmin(admin.ModelAdmin):
    list_display=['name','dob','gender','hobbie','religion','profession','qualification']

@admin.register(image)
class MovieAdmin(admin.ModelAdmin):
    list_display=['user']
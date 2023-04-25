from django.contrib import admin
from .models import Profile
# Register your models here.
# admin.site.register(Profile)
# @admin.register(Profile)
# class SProFileAdmin(admin.ModelAdmin):
#     list_display=["user","bio","location","birth_date","img"]
admin.site.register(Profile)
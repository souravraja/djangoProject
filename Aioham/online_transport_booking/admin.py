from django.contrib import admin
from .models import Transport,book_user,product
# Register your models here.
@admin.register(Transport)
class MovieAdmin(admin.ModelAdmin):
    list_display=['no','name']



@admin.register(book_user)
class MovieAdmin(admin.ModelAdmin):
    list_display=['name']



@admin.register(product)
class MovieAdmin(admin.ModelAdmin):
    list_display=['name']


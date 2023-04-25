from django.contrib import admin
from .models import CreateBook,Category

# Register your models here.

@admin.register(CreateBook)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display=['Book_name','Author_name','Page_number','description','Category','Book_Image','document']

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display=['Name',"Category_Image"]
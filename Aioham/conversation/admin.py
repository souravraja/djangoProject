from django.contrib import admin
from .models import catagory,Post
# Register your models here.
@admin.register(catagory)
class conversationAdmin(admin.ModelAdmin):
    list_display=('id','catagory')

@admin.register(Post)
class conversationPostAdmin(admin.ModelAdmin):
    list_display=('id','title','text')
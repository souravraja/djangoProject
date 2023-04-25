from django.contrib import admin
from .models import Post,StoryPost
# Register your models here.
@admin.register(Post)
class SocialBlogAdmin(admin.ModelAdmin):
    list_display=["title","description","image","dateTime"]

@admin.register(StoryPost)
class SocialShortAdmin(admin.ModelAdmin):
    list_display=["img","video"]
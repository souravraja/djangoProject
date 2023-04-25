from django.contrib import admin
from .models import News,main_news
# Register your models here.
@admin.register(News)
class MovieAdmin(admin.ModelAdmin):
    list_display=['heading','publish_date']

    
@admin.register(main_news)
class MovieAdmin(admin.ModelAdmin):
    list_display=['heading','publish_date']

from django.contrib import admin
from .models import Product,Image,Ownshop,ShopCategory

# Register your models here.
@admin.register(ShopCategory)
class ModelAdmin(admin.ModelAdmin):
    list_display=["name"]

@admin.register(Product)
class ModelAdmin(admin.ModelAdmin):
    list_display=["id","shopname","product","price","product_image","product_details"]

@admin.register(Image)
class ModelAdmin(admin.ModelAdmin):
    list_display=["Product","Image"]

@admin.register(Ownshop)
class ModelAdmin(admin.ModelAdmin):
    list_display=["id","type1","address","shop_name","shop_ownername","ph_no"]


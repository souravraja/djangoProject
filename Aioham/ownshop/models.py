from django.db import models

# Create your models here.
class ShopCategory(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Ownshop(models.Model):
    id=models.AutoField(primary_key=True)
    img=models.ImageField(upload_to='ownshoppic',null=True,blank=True)
    type1=models.ForeignKey(ShopCategory,on_delete=models.CASCADE,default=None)
    address=models.CharField(max_length=1000)
    shop_name=models.CharField(max_length=100)
    shop_ownername=models.CharField(max_length=100)
    ph_no=models.IntegerField()
    def __str__(self):
        return self.shop_name


class Product(models.Model):
    shopname=models.ForeignKey(Ownshop,on_delete=models.CASCADE,default=None)
    product=models.CharField(max_length=100)
    price=models.IntegerField()
    product_details=models.TextField(default=None,null=True,blank=True)
    product_image=models.ImageField(upload_to='productimage/',null=True,blank=True)
    def __str__(self):
        return self.product


class Image(models.Model):
    Product=models.ForeignKey(Product,on_delete=models.CASCADE)
    Image=models.ImageField(upload_to="imagefolder",null=True,blank=True)

from django.db import models

# Create your models here.

class Category(models.Model):
    Name=models.CharField(max_length=100,default=None)
    Category_Image=models.ImageField(upload_to="mainfloder1/",null=True,blank=True)
    def _str_(self):
        return self.Name

class CreateBook(models.Model):
    Book_name=models.CharField(max_length=100)
    Author_name=models.CharField(max_length=100,null=True,blank=True)
    Page_number=models.IntegerField(null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,default=True)
    Book_Image=models.ImageField(upload_to="mainfloder/",null=True,blank=True)
    document = models.FileField(upload_to='doc/',default=None,null=True,blank=True)

    def _str_(self):
        return self.Book_name
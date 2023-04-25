from django.db import models

# Create your models here.
class catagory(models.Model):
    catagory=models.CharField(max_length=50)
    def __str__(self):
        return self.catagory


class Post(models.Model):
    catagory=models.ForeignKey(catagory,on_delete=models.CASCADE)
    title=models.CharField(max_length=40)
    text=models.CharField(max_length=375)
    def __str__(self):
        return self.title

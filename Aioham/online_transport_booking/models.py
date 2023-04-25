from django.db import models

# Create your models here.
class Transport(models.Model):
    no=models.IntegerField()
    name=models.CharField(max_length=100)
    mobileno=models.IntegerField()
    start_location=models.CharField(max_length=100)
    sart_time=models.DateTimeField()
    end_location=models.CharField(max_length=100)
    end_time=models.DateTimeField()


class book_user(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    mobileno=models.IntegerField()

    def __str__(self):
        return self.name


class product(models.Model):
    owner=models.ForeignKey(book_user,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    size=models.CharField(max_length=50)
    weight=models.FloatField()
    def __str__(self):
        return self.name

    




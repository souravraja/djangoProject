from django.db import models

# Create your models here.

class Parlour_Facilitie(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Employee(models.Model):
    name=models.CharField(max_length=100)
    img=models.ImageField(upload_to="imgfolder")
    experience=models.IntegerField()
    expert=models.ManyToManyField(Parlour_Facilitie)
    def __str__(self):
        return self.name


class Parlour(models.Model):
    Name=models.CharField(max_length=100)
    Employee_name=models.ManyToManyField(Employee)
    Ph_no=models.IntegerField()
    Facilities=models.ManyToManyField(Parlour_Facilitie)
    Oping_Time=models.DateTimeField()
    def __str__(self):
        return self.Name


class User1(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    time=models.DateField()




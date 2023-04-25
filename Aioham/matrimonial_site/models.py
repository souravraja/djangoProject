from django.db import models

# Create your models here.
class matrimonial(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()
    gender=models.CharField(max_length=30)
    hobbie=models.TextField()
    profession=models.CharField(max_length=100)
    religion=models.CharField(max_length=100)
    qualification=models.CharField(max_length=20)
    profile_pic=models.ImageField(upload_to='matrimonial_main_image',null=True,blank=True)
    def __str__(self):
        return self.name

class image(models.Model):
    user=models.ForeignKey(matrimonial,on_delete=models.CASCADE)
    img1=models.ImageField(upload_to="matrimonial_image",null=True,blank=True)


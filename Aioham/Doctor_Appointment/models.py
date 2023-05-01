from django.db import models

# Create your models here.

class Dieases(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    def __str__(self):
        return self.name
class Doctor(models.Model):
    doctor_name=models.CharField(max_length=100,null=True,blank=True)
    doctor_image=models.ImageField(upload_to="doctorimage/",blank=True,null=True)
    experience=models.IntegerField(null=True,blank=True)
    license=models.FileField(upload_to="doctordocument/",null=True,blank=True)
    license_image=models.ImageField(upload_to="licenseimage/",blank=True,null=True)
    specalist=models.ForeignKey(Dieases,on_delete=models.CASCADE,default=True)
    def __str__(self):
        return self.doctor_name
    
class Doctor_Address(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,default=True)
    chamber=models.TextField(null=True,blank=True)
    pinnumber=models.IntegerField()
    opinngtime=models.TimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    closingtime=models.TimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    def __str__(self):
        return self.chamber
BLOOD_GROUP=(
    ("AB","AB+"),
    ("B","B+"),
    ("A","A+"),
    ("O","O+")
)

class Appointment(models.Model):
    patient_name=models.CharField(max_length=100,null=True,blank=True)
    patient_age=models.IntegerField(null=True,blank=True)
    bloodgroup=models.CharField(choices=BLOOD_GROUP,max_length=100,null=True,blank=True)
    appointment_date=models.DateTimeField(auto_now_add=False)
    doctor_name=models.ForeignKey(Doctor,on_delete=models.CASCADE,default=True)
    def __str__(self):
        return self.patient_name
   
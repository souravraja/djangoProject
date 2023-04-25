from django.db import models


# Create your models here.

class EducationCategory(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=30)
    def __str__(self):
        return self.title
    
class EducationSubject(models.Model):
    category=models.ForeignKey(EducationCategory,on_delete=models.CASCADE)
    sub_name=models.CharField(max_length=25)
    def __str__(self):
        return self.sub_name

class EducationContent(models.Model):
    category=models.ForeignKey(EducationCategory,on_delete=models.CASCADE)
    title=models.CharField(max_length=60)
    description=models.TextField(default="")
    def __str__(self):
        return self.title 


class EducationTeamMember(models.Model):
    name=models.CharField(max_length=100)
    subject=models.ForeignKey(EducationSubject,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='education_team/',null=True,default=True)
    def __str__(self):
        return self.name

class EducationCourse(models.Model):
    subject=models.ForeignKey(EducationSubject,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(max_length=40)
    course_image=models.ImageField(upload_to='education_team/',null=True,default=True)
    def __str__(self):
        return self.title


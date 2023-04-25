from django.db import models
from django.contrib.auth.models import User 
from django.core.validators import FileExtensionValidator

# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=70,null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    # img=models.ImageField(upload_to="social_image/",null=True,blank=True)
    image=models.ImageField(upload_to="social_image/",null=True,blank=True)
    # video=models.FileField(upload_to="social_video/",blank=True,null=True)
    dateTime=models.DateTimeField(auto_now_add=True)



class StoryPost(models.Model):
    User=models.ForeignKey(User,on_delete=models.CASCADE)
    img=models.ImageField(upload_to='social_story',null=True,blank=True)
    video=models.FileField(upload_to='story_videos_uploaded',null=True,
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
from django.db import models
from django.contrib.auth.models import User
# # Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True,null=True)
    location = models.CharField(max_length=30, blank=True,null=True)
    birth_date = models.DateField(null=True, blank=True)
    img=models.ImageField(upload_to='profile_img/', blank=True,null=True)
    def __str__(self):
        return f'{self.user.username} Profile'
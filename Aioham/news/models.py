from django.db import models

# Create your models here.
class News(models.Model):
    heading=models.CharField(max_length=300)
    img=models.ImageField(upload_to="newsImage",blank=True,null=True)
    publish_date=models.DateTimeField()
    news=models.TextField()

    def __str__(self):
        return self.heading


class main_news(News):
    def __str__(self):
        return self.heading
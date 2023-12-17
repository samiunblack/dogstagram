from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Hashtag(models.Model):
    name = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.ImageField(upload_to='temp/')
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    upload_time = models.DateTimeField(auto_now_add=True)
    hashtags = models.ManyToManyField(Hashtag, related_name='posts', blank=True)

    
    def __str__(self):
        return f'{self.upload_time.strftime("%B %d, %Y")} | {self.owner.username}'
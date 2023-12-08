from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, max_length=101)
    pfp = models.URLField(default="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/65761296352685.5eac4787a4720.jpg")
    followers = models.ManyToManyField(User, related_name='following', blank=True)
    
    def __str__(self):
        return self.user.username
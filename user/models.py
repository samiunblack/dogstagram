from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following')
    bio = models.TextField(blank=True)
    pfp = models.URLField(default="https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/65761296352685.5eac4787a4720.jpg")
    
    # Provide unique related_name for the groups and user_permissions fields
    groups = models.ManyToManyField('auth.Group', related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username
    
    
    def save(self, *args, **kwargs):
        if not self.pk and not self.is_superuser:
            self.is_staff = False
        super().save(*args, **kwargs)
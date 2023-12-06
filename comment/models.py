from django.db import models
from django.contrib.auth.models import User
from post.models import Post

# Create your models here.
class Comment(models.Model):
    text = models.CharField(max_length=500)
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f'{self.comment_time.strftime("%B %d, %Y")} | {self.user.username}'
from django.db import models  
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post.title}"
class CustomUser(AbstractUser):
    def clean(self):
        super().clean()
        validate_password_strength(self.password)
   
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions',  
        blank=True,
    )
    



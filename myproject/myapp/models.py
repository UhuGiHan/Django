from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from datetime import datetime
class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.username
    
class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)  
    description = models.TextField(blank=True)  
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)  
    content = models.TextField()  
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now) 
    updated_at = models.DateTimeField(default=datetime.now)  
    views = models.IntegerField(default=0) 
    likes = models.IntegerField(default=0)  

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)   
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

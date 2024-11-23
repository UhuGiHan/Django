from django.db import models  
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength

    
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
    

class Post(models.Model):

    title = models.CharField(max_length=200)

    content = models.TextField()


    author = models.ForeignKey(User, on_delete=models.CASCADE)

  
    created_at = models.DateTimeField(auto_now_add=True)

   
    def __str__(self):
        return self.title

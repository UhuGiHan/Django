from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
<<<<<<< Updated upstream

=======
    updated_at = models.DateTimeField(null=True, blank=True)
    # Hàm __str__: Trả về tiêu đề bài viết khi in đối tượng Post.
>>>>>>> Stashed changes
    def __str__(self):
        return self.title

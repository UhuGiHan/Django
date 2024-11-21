# Import các module cần thiết từ Django.
from django.db import models  # Để sử dụng các trường (fields) cho model.
from django.contrib.auth.models import User  # Để sử dụng mô hình User cho trường author.
from django.contrib.auth.models import AbstractUser
from .validators import validate_password_strength

    
class CustomUser(AbstractUser):
    def clean(self):
        super().clean()
        validate_password_strength(self.password)
    # Thêm related_name để tránh xung đột với mô hình mặc định User
    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # Đổi tên nhóm cho CustomUser
        blank=True,
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission', 
        related_name='customuser_permissions',  # Đổi tên quyền cho CustomUser
        blank=True,
    )
    
# Định nghĩa model Post để lưu trữ thông tin bài viết.
class Post(models.Model):
    # Trường title: tiêu đề bài viết, giới hạn độ dài tối đa là 200 ký tự.
    title = models.CharField(max_length=200)

    # Trường content: nội dung bài viết, có thể chứa văn bản dài không giới hạn.
    content = models.TextField()

    # Trường author: liên kết với model User, mỗi bài viết sẽ có một tác giả (user).
    # on_delete=models.CASCADE có nghĩa là khi người dùng bị xóa, bài viết cũng sẽ bị xóa theo.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # Trường created_at: lưu trữ thời gian bài viết được tạo, tự động điền khi bài viết được tạo.
    created_at = models.DateTimeField(auto_now_add=True)

    # Hàm __str__: Trả về tiêu đề bài viết khi in đối tượng Post.
    def __str__(self):
        return self.title

from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.models import User  
from .models import Post  
from django.contrib import messages  
from django.contrib.auth.decorators import login_required  
from django.utils.timezone import now  
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .forms import re


@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_superuser:
        post.delete()
        messages.success(request, "Bài viết đã được xóa thành công.")
    else:
        messages.error(request, "Bạn không có quyền xóa bài viết này.")
    return redirect('index')

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myapp/index.html', {'posts': posts, 'user': request.user})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'myapp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        if password != password_confirm:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'myapp/register.html')
        
        if not re.search(r'[A-Z]', password):  
            messages.error(request, 'Mật khẩu phải chứa ít nhất một chữ cái viết hoa.')
            return render(request, 'myapp/register.html')
        
        if not re.search(r'[0-9]', password):  
            messages.error(request, 'Mật khẩu phải chứa ít nhất một số.')
            return render(request, 'myapp/register.html')

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):  
            messages.error(request, 'Mật khẩu phải chứa ít nhất một ký tự đặc biệt.')
            return render(request, 'myapp/register.html')

        try:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('login')
        except:
            messages.error(request, 'Username already exists.')

    return render(request, 'myapp/register.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def create_post(request):
    
    if request.method == 'POST':
        title = request.POST['title']  
        content = request.POST['content']  
        author = request.user  
        Post.objects.create(title=title, content=content, author=author, created_at=now())
        messages.success(request, 'Bài viết của bạn đã được đăng thành công.')
        return redirect('index')
    return render(request, 'myapp/create_post.html')

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Post
from django.contrib import messages

def index(request):
    posts = Post.objects.all()
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
        if password == password_confirm:
            try:
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
            except:
                messages.error(request, 'Username already exists.')
        else:
            messages.error(request, 'Passwords do not match.')
    return render(request, 'myapp/register.html')

def logout_view(request):
    logout(request)
    return redirect('index')

from django.utils.timezone import now
from django.contrib.auth.decorators import login_required

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user  # Lấy username của người đang đăng nhập
        if title and content:
            Post.objects.create(title=title, content=content, author=author, created_at=now())
            return redirect('index')
        else:
            messages.error(request, 'Vui lòng điền đầy đủ tiêu đề và nội dung.')
    return render(request, 'myapp/create_post.html')

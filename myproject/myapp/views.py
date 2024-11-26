from django.contrib.auth import authenticate, login, logout  
from django.contrib.auth.models import User    
from django.contrib import messages  
from django.contrib.auth.decorators import login_required  
from django.utils.timezone import now  
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
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
            messages.error(request, 'Tên người dùng hoặc mật khẩu không hợp lệ.')
    return render(request, 'myapp/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        
        if password != password_confirm:
            messages.error(request, 'Mật khẩu không khớp.')
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
            messages.success(request, 'Đăng ký thành công. Vui lòng đăng nhập.')
            return redirect('login')
        except:
            messages.error(request, 'Tên người dùng đã tồn tại.')

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
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()  
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_id=post.id)

    context = {
        'post': post,
        'comments': comments,
        'form': form,
    }
    return render(request, 'myapp/post_detail.html', {'post': post})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.author or request.user.is_superuser:
        comment.delete()
    return redirect('post_detail', post_id=comment.post.id)
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        content = request.POST.get('content')  
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
        return redirect('post_detail', post_id=post.id)

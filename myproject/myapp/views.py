# Import các module cần thiết từ Django.
from django.shortcuts import render, redirect  # render: để trả về trang HTML, redirect: để chuyển hướng URL.
from django.contrib.auth import authenticate, login, logout  # authenticate: xác thực người dùng, login: đăng nhập, logout: đăng xuất.
from django.contrib.auth.models import User  # Đối tượng User dùng để quản lý người dùng.
from .models import Post  # Import mô hình Post (bài viết) từ models của ứng dụng.
from django.contrib import messages  # Để hiển thị thông báo cho người dùng.
from django.contrib.auth.decorators import login_required  # Đảm bảo người dùng đã đăng nhập trước khi truy cập vào view.
from django.utils.timezone import now  # Để lấy thời gian hiện tại.

# Hàm xử lý trang chủ (hiển thị danh sách bài viết).
def index(request):
    # Lấy tất cả các bài viết và sắp xếp theo thời gian tạo (bài viết mới nhất ở đầu).
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'myapp/index.html', {'posts': posts, 'user': request.user})

# Hàm xử lý đăng nhập.
def login_view(request):
    # Nếu người dùng gửi form đăng nhập (POST request).
    if request.method == 'POST':
        # Lấy thông tin username và password từ form.
        username = request.POST['username']
        password = request.POST['password']
        # Kiểm tra xem thông tin đăng nhập có chính xác không.
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Nếu thông tin đăng nhập đúng, đăng nhập người dùng và chuyển hướng đến trang chủ.
            login(request, user)
            return redirect('index')
        else:
            # Nếu thông tin sai, hiển thị thông báo lỗi.
            messages.error(request, 'Invalid username or password.')
    return render(request, 'myapp/login.html')

# Hàm xử lý đăng ký tài khoản mới.
def register_view(request):
    # Nếu người dùng gửi form đăng ký (POST request).
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        # Kiểm tra xem mật khẩu có khớp không.
        if password == password_confirm:
            try:
                # Tạo tài khoản người dùng mới.
                User.objects.create_user(username=username, password=password)
                messages.success(request, 'Registration successful. Please log in.')
                return redirect('login')
            except:
                # Nếu username đã tồn tại, hiển thị thông báo lỗi.
                messages.error(request, 'Username already exists.')
        else:
            # Nếu mật khẩu không khớp, hiển thị thông báo lỗi.
            messages.error(request, 'Passwords do not match.')
    return render(request, 'myapp/register.html')

# Hàm xử lý đăng xuất.
def logout_view(request):
    # Đăng xuất người dùng và chuyển hướng về trang chủ.
    logout(request)
    return redirect('index')

# Hàm xử lý tạo bài viết mới (chỉ cho người dùng đã đăng nhập).
@login_required  # Chỉ cho phép người dùng đã đăng nhập mới có thể tạo bài viết.
def create_post(request):
    # Nếu người dùng gửi form tạo bài viết (POST request).
    if request.method == 'POST':
        title = request.POST['title']  # Lấy tiêu đề bài viết.
        content = request.POST['content']  # Lấy nội dung bài viết.
        author = request.user  # Lấy tác giả là người dùng hiện tại.
        # Tạo bài viết mới trong cơ sở dữ liệu.
        Post.objects.create(title=title, content=content, author=author, created_at=now())
        messages.success(request, 'Bài viết của bạn đã được đăng thành công.')
        return redirect('index')
    return render(request, 'myapp/create_post.html')

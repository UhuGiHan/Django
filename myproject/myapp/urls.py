# Import module path từ Django để định nghĩa các URL, và views từ file views của ứng dụng.
from django.urls import path
from . import views  # Import các view functions từ file views của ứng dụng hiện tại.

# Danh sách các URL patterns của ứng dụng.
urlpatterns = [
    # Định nghĩa đường dẫn cho trang chủ (index).
    path('', views.index, name='index'),  # Đường dẫn trống ('') sẽ gọi view index() để hiển thị trang chủ.

    # Định nghĩa đường dẫn cho trang đăng nhập (login).
    path('login/', views.login_view, name='login'),  # Đường dẫn 'login/' sẽ gọi view login_view() để xử lý đăng nhập.

    # Định nghĩa đường dẫn cho trang đăng ký (register).
    path('register/', views.register_view, name='register'),  # Đường dẫn 'register/' sẽ gọi view register_view() để xử lý đăng ký.

    # Định nghĩa đường dẫn cho trang đăng xuất (logout).
    path('logout/', views.logout_view, name='logout'),  # Đường dẫn 'logout/' sẽ gọi view logout_view() để xử lý đăng xuất người dùng.

    # Định nghĩa đường dẫn cho trang tạo bài viết (create-post).
    path('create-post/', views.create_post, name='create_post'),  # Đường dẫn 'create-post/' sẽ gọi view create_post() để tạo bài viết mới.

    path('', views.index, name='index'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]


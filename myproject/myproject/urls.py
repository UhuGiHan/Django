"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import các module cần thiết từ Django.
from django.contrib import admin  # Quản lý admin của Django
from django.urls import path, include  # path: Để định nghĩa các đường dẫn URL, include: Để kết nối với các file URLs khác

# Danh sách các URL patterns của ứng dụng.
urlpatterns = [
    # Đường dẫn tới trang admin của Django.
    path('admin/', admin.site.urls),  # Định nghĩa đường dẫn cho trang admin, nơi quản trị viên có thể đăng nhập và quản lý dữ liệu.

    # Kết nối với các URL patterns trong app 'myapp'.
    path('', include('myapp.urls')),  # Định nghĩa đường dẫn gốc (trang chủ) và liên kết tới các URL của ứng dụng 'myapp'.
]


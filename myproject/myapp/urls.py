from django.urls import path
from . import views 


urlpatterns = [
    
    path('', views.index, name='index'),  
    path('login/', views.login_view, name='login'), 
    path('register/', views.register_view, name='register'),  
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/add_comment/', views.add_comment, name='add_comment'),
    path('logout/', views.logout_view, name='logout'),  
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('create-post/', views.create_post, name='create_post'),  
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]


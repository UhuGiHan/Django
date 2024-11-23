from django.urls import path
from . import views 


urlpatterns = [
    
    path('', views.index, name='index'),  
    
    path('login/', views.login_view, name='login'), 
    
    path('register/', views.register_view, name='register'),  

    
    path('logout/', views.logout_view, name='logout'),  

    
    path('create-post/', views.create_post, name='create_post'),  
    path('', views.index, name='index'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]


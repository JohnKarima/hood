from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('',views.index, name = 'index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('update/', views.update, name='update'),
    path('upload_post/', views.upload_post, name='upload_post'),
    path('post/<post_id>/',views.post,name ='post'),
]